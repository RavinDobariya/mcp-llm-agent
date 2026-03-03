import os
from anthropic import AsyncAnthropic

"""
we passing MCPserrvice object to Agent class to access MCPserrvice methods via mcp.method()

response.content = [
    TextBlock(...),     #text
    ToolUseBlock(...),
    ...
]

it contains all the messages from Claude
"""

class Agent:
    def __init__(self, mcp):
        self.mcp = mcp
        self.client = AsyncAnthropic(
            api_key=os.getenv("ANTHROPIC_API_KEY")
        )

    async def run(self, user_input: str) -> str:

        response = await self.client.messages.create(
            model="claude-3-5-sonnet-20241022",
            max_tokens=500,
            messages=[
                {"role": "user", "content": user_input}
            ],
            tools=self.mcp.get_tools_schema()           # give access to tools
        )

        # If Claude wants to use tool
        for block in response.content:              # or response.content[0].type == "tool_use"
            if block.type == "tool_use":
                tool_name = block.name
                tool_input = block.input

            tool_result = await self.mcp.call_tool(tool_name, tool_input)

            # Send tool result back to Claude for final answer
            followup = await self.client.messages.create(
                model="claude-3-5-sonnet-20241022",
                max_tokens=500,
                messages=[
                    {"role": "user", "content": user_input},
                    response.content[0],
                    {
                        "role": "tool",
                        #"tool_use_id": tool_call.id,
                        "content": str(tool_result)
                    }
                ]
            )

            return followup.content[0].text

        # if Claude did not use tool
        return response.content[0].text