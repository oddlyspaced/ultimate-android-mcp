from mcp.server.fastmcp import FastMCP
from src.adbutils import get_all_packages, get_system_packages, get_user_packages

# Create an MCP server
mcp = FastMCP("Android MCP")


# Tool: Get list of all installed packages
@mcp.tool()
def all_packages() -> list[str]:
    """Get list of all packages in the connected Android device"""
    return get_all_packages()


# Tool: Get list of all user installed packages
@mcp.tool()
def user_packages() -> list[str]:
    """Get list of all user installed packages in the connected Android device"""
    return get_user_packages()


# Tool: Get list of all user installed packages
@mcp.tool()
def system_packages() -> list[str]:
    """Get list of all system packages in the connected Android device"""
    return get_system_packages()
