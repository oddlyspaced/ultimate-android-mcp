from mcp.server.fastmcp import FastMCP
from src.device_manager import DeviceManager
from config import AndroidMCPConfig

config = AndroidMCPConfig()
handler = DeviceManager(config)

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


@mcp.tool()
def get_current_ui_labels() -> list:
    """Gets the text labels that is being shown on the screen currently in the connected Android device. Use the text and context-desc property in this as reference to the content being displayed on screen and use it to click on elements. Each node contains the following information: text, bounds: the bounding box, focused: is it focused currently, checkable: can it be checked, clickable: can it be clicked, focusable: can it be focused, long-clickable: is it long clickable, selected: can it be selected"""
    return handler.get_current_ui_labels()


# @mcp.tool()
# def get_current_clickable_nodes() -> list:
#     """Gets the nodes that are currently displayed on the screen that can be interacted with by clicking in the connected Android device"""
#     return handler.get_current_ui_labels()


@mcp.tool()
def get_current_focused_nodes() -> list:
    """Gets the nodes that are currently focused in the user interface in the connected Android device"""
    return handler.get_current_focused_nodes()


@mcp.tool()
def input_tap(x: int, y: int):
    """Taps on the screen at a given X Y co ordinate in the connected Android device"""
    handler.input_tap(x, y)


@mcp.tool()
def input_text(text: str):
    """Simulates keyboard for the given text string in the connected Android device"""
    handler.input_text(text)


@mcp.tool()
def is_keyboard_open():
    """Checks if the system keyboard is open currently in the connected Android device"""
    return handler.is_keyboard_open()


@mcp.tool()
def execute_adb_shell(command: str):
    """Executes an ADB command on the connected Android device"""
    handler.execute_adb_shell(command)


if __name__ == "__main__":
    mcp.run(transport="stdio")
