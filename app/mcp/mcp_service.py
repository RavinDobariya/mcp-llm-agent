from mcp import ClientSession
from mcp.client.stdio import stdio_client


class MCPService:
    def __init__(self):
        self.session = None
        self.tools = []

    async def connect(self):
        self.transport = await stdio_client("python", ["app/server.py"])    # Start MCP server as a subprocess => enable agent to communicate with server
        self.session = await ClientSession(self.transport).__aenter__()     # Provide builtin method => list_tools & call_tool

        # Load available tools from server
        tools_response = await self.session.list_tools()
        self.tools = tools_response.tools

    async def call_tool(self, name: str, arguments: dict):
        return await self.session.call_tool(name, arguments)

    async def close(self):
        await self.session.__aexit__(None, None, None)

    #provide tool schema to claude
    def get_tools_schema(self):
        return self.tools


"""
On call tool =>  @mcp.tool() -> async def web_search(query: str):


"""