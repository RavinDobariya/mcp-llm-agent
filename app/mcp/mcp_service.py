import asyncio
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client

from app.mcp.tools import tools
from app.tools.registry import TOOL_MAP


class MCPService:
    def __init__(self):
        self.session = None
        self._stdio = None

    async def connect(self):
        server_params = StdioServerParameters(
            command="npx",
            args=["-y", "@modelcontextprotocol/server-anthropic"]
        )

        self._stdio = stdio_client(server_params)
        read, write = await self._stdio.__aenter__()

        self.session = await ClientSession(read, write).__aenter__()
        await self.session.initialize()

        # ✅ REGISTER TOOLS TO MCP
        await self.session.set_tools(tools)

        print("✅ MCP session ready")

    async def ask(self, query: str) -> str:
        # 1️⃣ First call to Claude
        response = await self.session.create_message(
            messages=[{"role": "user", "content": query}],
            max_tokens=300
        )

        content = response.content[0]

        # 🛠 TOOL USE CASE
        if content.type == "tool_use":
            tool_name = content.name
            tool_input = content.input

            # run tool in python
            tool_result = await TOOL_MAP[tool_name](**tool_input)

            # 2️⃣ Send tool result back to Claude
            final_response = await self.session.create_message(
                messages=[
                    {"role": "user", "content": query},
                    response,
                    {
                        "role": "tool",
                        "name": tool_name,
                        "content": tool_result
                    }
                ],
                max_tokens=300
            )

            return final_response.content[0].text

        # 💬 Normal text response
        final_text = []
        for block in response.content:
            if block.type == "text":
                final_text.append(block.text)

        return "\n".join(final_text)

    async def close(self):
        if self.session:
            await self.session.__aexit__(None, None, None)
        if self._stdio:
            await self._stdio.__aexit__(None, None, None)