# from mcp.server.fastmcp import FastMCPServer
# from mcp.server.fastmcp import FastMCPHandler
# from mcp.server.fastmcp import FastMCPRequest
from mcp.server.fastmcp import FastMCP

mcp = FastMCP("Weather")

@mcp.tool()
def get_weather(location: str) -> str:
    """Get the current weather for a given location."""
    # In a real implementation, you would call a weather API here.
    # For this example, we'll just return a dummy weather report.
    return f"The current weather in {location} is sunny with a high of 25°C."

if __name__ == "__main__":
    mcp.run()