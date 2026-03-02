from app.llm.claude_client import ask_claude
from app.llm.build_prompt import build_prompt
from app.tools.registry import TOOL_MAP

class Agent:
    def __init__(self, mcp_service):
        self.mcp = mcp_service

    async def run(self, query: str) -> str:
        return await self.mcp.ask(query)

""""    
def run_agent(query: str) -> str:
    messages = [
        {"role": "user", "content": build_prompt(query)}
    ]

    response = ask_claude(messages)

    content = response.content[0]

    # 🧠 If Claude calls a tool
    if content.type == "tool_use":
        tool_name = content.name
        tool_input = content.input

        tool_result = TOOLS[tool_name](**tool_input)

        return f"[TOOL USED: {tool_name}]\n{tool_result}"

    # 💬 Normal text response
    return content.text

"""
"""
{
  "type": "tool_use",
  "name": "web_search",
  "input": {
    "query": "latest AI news"
  }
tool_result = web_search(query="latest AI news")
"""