from mcp.server.fastmcp import FastMCP
from app.tools.registry import register_tools as customize_tools

mcp = FastMCP("my-dev-tools")

# 🔧 Register all tools
customize_tools(mcp)



if __name__ == "__main__":
    mcp.run()