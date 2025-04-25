from mcp.server.fastmcp import FastMCP
from ppadb.client import Client as AdbClient
from src.device_manager import DeviceHandler

client = AdbClient(host="127.0.0.1", port=5037)
devices = client.devices()

# create reference to first connected adb device
handler = DeviceHandler(devices[0])

# Create an MCP server
mcp = FastMCP("Android MCP")


# Tool: Get list of all installed packages
@mcp.tool()
def all_packages() -> list[str]:
    """Get list of all packages in the connected Android device"""
    return handler.get_all_packages()


# Tool: Get list of all user installed packages
@mcp.tool()
def user_packages() -> list[str]:
    """Get list of all user installed packages in the connected Android device"""
    return handler.get_user_packages()


# Tool: Get list of all user installed packages
@mcp.tool()
def system_packages() -> list[str]:
    """Get list of all system packages in the connected Android device"""
    return handler.get_system_packages()
