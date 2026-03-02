from anthropic import Anthropic
from app.tools.registry import TOOL_MAP as tool_definitions

from app.config.settings import ANTHROPIC_API_KEY, MODEL

client = Anthropic(api_key=ANTHROPIC_API_KEY)

def ask_claude(messages):
    response = client.messages.create(
        model=MODEL,
        max_tokens=500,
        tools=tool_definitions,
        messages=messages
    )

    return response