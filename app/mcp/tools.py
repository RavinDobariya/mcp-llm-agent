from mcp.types import Tool

tools = [
    Tool(
        name="web_search",
        description="Search the web for latest information",
        inputSchema={
            "type": "object",
            "properties": {
                "query": {"type": "string"}
            },
            "required": ["query"]
        }
    )
]