from mcp.server.fastmcp import FastMCP
import os

mcp = FastMCP("LocalNotes")

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
NOTES_FILE = os.path.join(BASE_DIR, "notes.txt")

@mcp.tool()
def add_not_to_file(content: str) -> str:
    """
    Appends the given content to the user's local notes.
    Args:
        content (str): The content to be added to the file.
    """
    file = NOTES_FILE
    try:
        with open(file, "a", encoding="utf-8") as f:
            f.write(content + "\n")
        return f"Content added to {file}."
    except Exception as e:
        return f"Error adding content to {file}: {e}"
    
@mcp.tool()
def read_notes() -> str:
    """
    Reads the content of the user's local text file and returns it.
    """
    file = NOTES_FILE
    try:
        with open(file, "r", encoding="utf-8") as f:
            content = f.read()
        return content if content else "The notes file is empty."
    except Exception as e:
        return f"Error reading {file}: {e}"
    
if __name__ == "__main__":
    mcp.run(transport="stdio")