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
    """Returns a list of all packages (both system and user-installed) currently installed on the connected Android device."""
    return handler.get_all_packages()


# Tool: Get list of all user installed packages
@mcp.tool()
def user_packages() -> list[str]:
    """Returns a list of user-installed application package names on the connected Android device."""
    return handler.get_user_packages()


# Tool: Get list of all system installed packages
@mcp.tool()
def system_packages() -> list[str]:
    """Returns a list of system application package names (pre-installed apps) on the connected Android device."""
    return handler.get_system_packages()


# Tool: Launch an app via its package name
@mcp.tool()
def launch_app(package_name: str) -> str:
    """Launches the app with the specified package name on the connected Android device. Returns a success or error message."""
    try:
        handler.launch_app(package_name)
        return f"Successfully Launched {package_name}"
    except:
        return f"Error Launching {package_name}"


# Tool: Get all the visible text label nodes on the screen
@mcp.tool()
def get_current_ui_labels() -> list:
    """Returns a list of UI nodes currently visible on the device screen, focusing on text labels and content descriptions. Each node contains properties like text, bounds, clickable, focusable, and others."""
    return handler.get_current_ui_labels()


# Tool: Get all the focused nodes
@mcp.tool()
def get_current_focused_nodes() -> list:
    """Returns a list of UI nodes that are currently focused on the connected Android device screen."""
    return handler.get_current_focused_nodes()


# Tool: Tap on the screen at X Y coordinates
@mcp.tool()
def input_tap(x: int, y: int):
    """Simulates a tap gesture at the specified (x, y) coordinates on the connected Android device screen."""
    handler.input_tap(x, y)


# Tool: Input text
@mcp.tool()
def input_text(text: str):
    """Simulates typing the given text input into the currently focused field on the connected Android device."""
    handler.input_text(text)


# Tool: Detect if keyboard is open
@mcp.tool()
def is_keyboard_open():
    """Checks if the virtual keyboard is currently open on the connected Android device."""
    return handler.is_keyboard_open()


# Tool: Execute an ADB shell command on the device
@mcp.tool()
def execute_adb_shell(command: str):
    """Executes a raw ADB shell command on the connected Android device and returns the output."""
    return handler.execute_adb_shell(command)


if __name__ == "__main__":
    mcp.run(transport="stdio")
