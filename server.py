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


@mcp.tool()
def launch_app(package_name: str) -> str:
    """Launches an app with the given package name in the connected Android device"""
    try:
        handler.launch_app(package_name)
        return f"Successfully Launched {package_name}"
    except:
        return f"Error Launching {package_name}"


if __name__ == "__main__":
    mcp.run(transport="stdio")
