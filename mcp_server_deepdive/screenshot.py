from mcp.server.fastmcp import FastMCP
import pyautogui
import io
from mcp.server.fastmcp.utilities.types import Image

mcp = FastMCP("Screenshot Demo")

@mcp.tool()
def take_screenshot() -> Image:
    """
    Takes a screenshot of the current screen and returns it as an image.
    Use this tool whenever a user asks to take a screenshot or when you need to capture the current screen for any reason.
    """
    buffer = io.BytesIO()
    # If the file exceeds 1MB, it'll be rejected by Claude
    screenshot = pyautogui.screenshot()
    screenshot.convert("RGB").save(buffer, format="JPEG", quality=60, optimize=True)
    buffer.seek(0)
    return Image(data=buffer.getvalue(), format="jpeg")

if __name__ == "__main__":
    mcp.run(transport="stdio")