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
    """Returns a list of all packages (both system and user-installed) currently installed on the connected Android device. No parameters are required."""
    return handler.get_all_packages()


# Tool: Get list of all user installed packages
@mcp.tool()
def user_packages() -> list[str]:
    """Returns a list of user-installed application package names on the connected Android device. No parameters are required."""
    return handler.get_user_packages()


# Tool: Get list of all system installed packages
@mcp.tool()
def system_packages() -> list[str]:
    """Returns a list of system application package names (pre-installed apps) on the connected Android device. No parameters are required."""
    return handler.get_system_packages()


# Tool: Launch an app via its package name
@mcp.tool()
def launch_app(package_name: str) -> str:
    """Launches the app with the specified package name on the connected Android device. Requires the `package_name` parameter, which is the package name of the app to be launched."""
    try:
        handler.launch_app(package_name)
        return f"Successfully Launched {package_name}"
    except:
        return f"Error Launching {package_name}"


# Tool: Get all the visible text label nodes on the screen
@mcp.tool()
def get_current_ui_labels() -> list:
    """Returns a list of UI nodes currently visible on the device screen, focusing on text labels and content descriptions. Each node contains properties like text, bounds, clickable, focusable, and others. No parameters are required."""
    return handler.get_current_ui_labels()


# Tool: Get all the focused nodes
@mcp.tool()
def get_current_focused_nodes() -> list:
    """Returns a list of UI nodes that are currently focused on the connected Android device screen. No parameters are required."""
    return handler.get_current_focused_nodes()


# Tool: Input key event
@mcp.tool()
def input_keyevent(keycode: int):
    """Simulates a key event with the specified keycode on the connected Android device. Requires the `keycode` parameter, which is the keycode of the key to simulate."""
    return handler.input_keyevent(keycode)


# Tool: Input tap
@mcp.tool()
def input_tap(x: int, y: int):
    """Simulates a tap gesture at the specified (x, y) coordinates on the connected Android device screen. Requires `x` and `y` parameters, which are the coordinates of the tap."""
    return handler.input_tap(x, y)


# Tool: Input text
@mcp.tool()
def input_text(text: str):
    """Simulates typing the given text input into the currently focused field on the connected Android device. Requires the `text` parameter, which is the string to be typed."""
    return handler.input_text(text)


# Tool: Input press
@mcp.tool()
def input_press(keycode: int):
    """Simulates a key press event with the specified keycode on the connected Android device. Requires the `keycode` parameter, which is the keycode of the key to press."""
    return handler.input_press(keycode)


# Tool: Input roll
@mcp.tool()
def input_roll(dx: int, dy: int):
    """Simulates a rolling gesture with the specified dx and dy values on the connected Android device. Requires `dx` and `dy` parameters, which are the rolling distances in the x and y directions respectively."""
    return handler.input_roll(dx, dy)


# Tool: Input swipe
@mcp.tool()
def input_swipe(x1: int, y1: int, x2: int, y2: int, duration_ms: int = None):
    """Simulates a swipe gesture from (x1, y1) to (x2, y2) with an optional duration on the connected Android device. Requires `x1`, `y1`, `x2`, `y2` parameters for the start and end coordinates, and an optional `duration_ms` parameter for the swipe duration in milliseconds."""
    return handler.input_swipe(x1, y1, x2, y2, duration_ms)


# Tool: Check if keyboard is open
@mcp.tool()
def is_keyboard_open():
    """Checks if the virtual keyboard is currently open on the connected Android device. No parameters are required."""
    return handler.is_keyboard_open()


# Tool: Execute ADB shell command
@mcp.tool()
def execute_adb_shell(command: str):
    """Executes a raw ADB shell command on the connected Android device and returns the output. Requires the `command` parameter, which is the shell command to execute."""
    return handler.shell(command)


# Tool: Get CPU core count
@mcp.tool()
def cpu_count():
    """Returns the number of CPU cores on the connected Android device. No parameters are required."""
    return handler.cpu_count()


# Tool: Get CPU load percentage
@mcp.tool()
def cpu_percent():
    """Returns the current CPU load percentage on the connected Android device. No parameters are required."""
    return handler.cpu_percent()


# Tool: Get device serial number
@mcp.tool()
def get_serial_no():
    """Returns the serial number of the connected Android device. No parameters are required."""
    return handler.get_serial_no()


# Tool: Get device properties
@mcp.tool()
def get_properties():
    """Returns the build.prop properties of the connected Android device. No parameters are required."""
    return handler.get_properties()


# Tool: List device features
@mcp.tool()
def list_features():
    """Returns the device overlay configuration properties of the connected Android device. No parameters are required."""
    return handler.list_features()


# Tool: Get battery level
@mcp.tool()
def get_battery_level():
    """Returns the battery level of the connected Android device. No parameters are required."""
    return handler.get_battery_level()


# Tool: Get screen density
@mcp.tool()
def wm_density():
    """Returns the screen density of the connected Android device. No parameters are required."""
    return handler.wm_density()


# Tool: Get screen size
@mcp.tool()
def wm_size():
    """Returns the screen size of the connected Android device. No parameters are required."""
    return handler.wm_size()


# Tool: Pull file from device
@mcp.tool()
def pull_file(remote: str, local: str):
    """Pulls a file from the connected Android device to the local machine. Requires `remote` and `local` parameters, which are the paths of the file on the device and the local machine respectively."""
    return handler.pull(remote, local)


# Tool: Push file to device
@mcp.tool()
def push_file(local: str, remote: str):
    """Pushes a file from the local machine to the connected Android device. Requires `local` and `remote` parameters, which are the paths of the file on the local machine and the device respectively."""
    return handler.push(local, remote)


# Tool: Get process ID by package name
@mcp.tool()
def get_pid(package_name: str):
    """Returns the process ID (PID) for the specified package name on the connected Android device. Requires the `package_name` parameter, which is the name of the package to query."""
    return handler.get_pid(package_name)


# Tool: Get top activities
@mcp.tool()
def get_top_activities():
    """Returns the activities currently on top on the connected Android device. No parameters are required."""
    return handler.get_top_activities()


# Tool: Get top activity
@mcp.tool()
def get_top_activity():
    """Returns the singular activity currently on top on the connected Android device. No parameters are required."""
    return handler.get_top_activity()


# Tool: Install APK
@mcp.tool()
def install_apk(apk_path: str):
    """Installs an APK on the connected Android device. Requires the `apk_path` parameter, which is the path to the APK file to be installed."""
    return handler.install(apk_path)


# Tool: Uninstall package
@mcp.tool()
def uninstall_package(package_name: str):
    """Uninstalls the specified package from the connected Android device. Requires the `package_name` parameter, which is the name of the package to uninstall."""
    return handler.uninstall(package_name)


# Tool: Check if package is installed
@mcp.tool()
def is_installed(package_name: str):
    """Checks if the specified package is installed on the connected Android device. Requires the `package_name` parameter, which is the name of the package to check."""
    return handler.is_installed(package_name)


# Tool: Get all packages
@mcp.tool()
def get_all_packages(
    user_installed_only: bool = False, system_installed_only: bool = False
):
    """Returns a list of all packages on the connected Android device, with optional filters for user-installed or system-installed packages. Accepts `user_installed_only` and `system_installed_only` as optional boolean parameters to filter the results."""
    return handler.get_all_packages(user_installed_only, system_installed_only)


# Tool: Get system packages
@mcp.tool()
def get_system_packages():
    """Returns a list of system-installed packages on the connected Android device. No parameters are required."""
    return handler.get_system_packages()


# Tool: Get user packages
@mcp.tool()
def get_user_packages():
    """Returns a list of user-installed packages on the connected Android device. No parameters are required."""
    return handler.get_user_packages()


# Tool: Launch app
@mcp.tool()
def launch_app(package_name: str):
    """Launches the specified app on the connected Android device. Requires the `package_name` parameter, which is the name of the app to launch."""
    return handler.launch_app(package_name)


if __name__ == "__main__":
    mcp.run(transport="stdio")
