from mcp import ClientSession, StdioServerParameters, types
from mcp.client.stdio import stdio_client
import asyncio
import traceback

# Try with airbnb MCP server

server_params = StdioServerParameters(
    command="npx",
    args = ["-y", "@openbnb/mcp-server-airbnb", "--ignore-robots-txt"] # Optional command line arguments
)

async def run():
    try:
        print("Starting stdio_client...")
        async with stdio_client(server_params) as (read, write):
            print("Client connected. Creating session...")
            async with ClientSession(read, write) as session:
                print("Initializing session...")
                await session.initialize()
                print("Listing tools...")
                tools = await session.list_tools()
                print("Available tools:", tools)
                print("Calling tools...")
                result = await session.call_tool("airbnb_search", arguments={"location": "New York"})
                print("Tool result:", result)
    except Exception as e:
        print("An error occurred:", e)
        traceback.print_exc()

if __name__ == "__main__":
    asyncio.run(run())
