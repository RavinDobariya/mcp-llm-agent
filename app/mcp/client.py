import asyncio
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client


async def run_mcp():
    server_params = StdioServerParameters(
        command="npx",
        args=[
            "-y",
            "@modelcontextprotocol/server-filesystem",
            "."
        ]
    )

    async with stdio_client(server_params) as (read, write):
        async with ClientSession(read, write) as session:
            await session.initialize()

            print("✅ MCP connected\n")

            # 🧠 Send a real prompt to Claude
            response = await session.create_message(
                messages=[
                    {
                        "role": "user",
                        "content": "Explain Model Context Protocol in simple words"
                    }
                ],
                max_tokens=300
            )

            print("🤖 Claude response:\n")

            for block in response.content:
                if block.type == "text":
                    print(block.text)


if __name__ == "__main__":
    asyncio.run(run_mcp())