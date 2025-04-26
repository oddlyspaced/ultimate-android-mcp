# Ultimate Android MCP

## Description
Ultimate Android MCP is a powerful and versatile MCP (Model Context Protocol) server designed to interact with connected Android devices. It provides a wide range of tools and functionalities to perform various tasks on Android devices, such as managing applications, interacting with the UI, retrieving device information, and more. This project aims to provide the widest set of capabilities to ensure optimal interaction via LLMs using the Model Context Protocol.

## Features
The MCP server provides the following features:

### Application Management
- Retrieve a list of all installed packages (system and user-installed).
- Retrieve a list of user-installed application package names.
- Retrieve a list of system application package names (pre-installed apps).
- Launch applications by package name.
- Install an APK on the connected Android device.
- Uninstall a specified package from the device.
- Check if a specified package is installed on the device.

### Input Simulation
- Simulate input events such as key presses, taps, swipes, and text input.
- Simulate a key event with a specified keycode.
- Simulate a tap gesture at specified (x, y) coordinates.
- Simulate typing text into the currently focused field.
- Simulate a key press event with a specified keycode.
- Simulate a rolling gesture with specified dx and dy values.
- Simulate a swipe gesture from one coordinate to another with an optional duration.
- Check if the virtual keyboard is currently open.

### Device Information
- Retrieve device-specific information, including serial number, properties, and battery level.
- Retrieve the serial number of the connected Android device.
- Retrieve build.prop properties of the device.
- Retrieve device overlay configuration properties.
- Retrieve the battery level of the device.
- Retrieve the screen density of the device.
- Retrieve the screen size of the device.

### System and Performance Monitoring
- Retrieve CPU information, such as core count and load percentage.
- Retrieve the number of CPU cores on the device.
- Retrieve the current CPU load percentage on the device.
- Retrieve top activities and processes.
- Retrieve the process ID (PID) for a specified package name.
- Retrieve the activities currently on top of the device.
- Retrieve the singular activity currently on top of the device.

### File Management
- Manage files on the device, including pushing and pulling files.
- Pull a file from the connected Android device to the local machine.
- Push a file from the local machine to the connected Android device.

### UI Interaction
- Retrieve UI elements and focused nodes from the device screen.
- Retrieve a list of UI nodes currently visible on the device screen, focusing on text labels and content descriptions.
- Retrieve a list of UI nodes that are currently focused on the device screen.

### Advanced Operations
- Execute raw ADB shell commands and retrieve the output.

## Prerequisites
To run this project, ensure you have the following:

- Python 3.12 or higher.
- ADB (Android Debug Bridge) installed and configured on your system.
- A connected Android device with USB debugging enabled.
- The `pure-python-adb` library installed (included in the project dependencies).

## Installation and Setup
Follow these steps to set up the project:

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd android-mcp-py
   ```

2. Create a virtual environment and activate it:
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate  # On Windows, use .venv\Scripts\activate
   ```

3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Configure the project by editing the `config.py` file to match your ADB setup and device details.

## Configuration Overview
The `config.py` file contains the following configuration options:

- `adb_client_host`: The host address of the ADB server (default: `127.0.0.1`).
- `adb_client_port`: The port of the ADB server (default: `5037`).
- `adb_device_serial`: The serial number or IP address of the connected device. If not specified, the first available device will be used.
- `device_temp_folder`: The temporary folder on the device for storing intermediate files (default: `/sdcard/.androidmcp`).

## Usage via Claude MCP Config JSON
To use the MCP server, you can interact with it via a Claude MCP configuration JSON. Here is an example configuration:

```json
{
  "transport": "stdio",
  "tools": [
    {
      "name": "all_packages",
      "description": "Retrieve a list of all installed packages."
    },
    {
      "name": "launch_app",
      "description": "Launch an app by its package name.",
      "parameters": {
        "package_name": "com.example.app"
      }
    },
    {
      "name": "input_tap",
      "description": "Simulate a tap gesture.",
      "parameters": {
        "x": 100,
        "y": 200
      }
    }
  ]
}
```

Run the MCP server using the following command:
```bash
python server.py
```

You can then use the tools defined in the JSON configuration to interact with the connected Android device.