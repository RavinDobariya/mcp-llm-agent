import asyncio
from app.mcp.mcp_service import MCPService
from app.llm.agent import Agent


async def main():
    mcp = MCPService()
    await mcp.connect()

    agent = Agent(mcp)

    print("🚀 MCP Agent running (type 'exit')\n")

    while True:
        user_input = input(">> ")

        if user_input.lower() == "exit":
            break

        result = await agent.run(user_input)

        print("\n🤖", result, "\n")

    await mcp.close()


if __name__ == "__main__":
    asyncio.run(main())