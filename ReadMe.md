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

## Demo
Physical device (Pixel 7 Pro running Android 15) connected via USB, which is having its screen shared via scrcpy. Using Claude for Desktop (Version 0.9.2). The text provided to Claude was the following :

```In the connected android device, play the song 'mask off' by future on spotify.```

Claude then figured out how to launch the app, which button to click and what text to enter where. Everything in the demo is autonomous with no user interaction in between.

// Add video here

## Prerequisites
To run this project, ensure you have the following:

- Python 3.
- ADB (Android Debug Bridge) installed and configured on your system (ensure that ```adb``` command works).
- A connected Android device with USB debugging enabled.
- The `pure-python-adb` library installed (included in the project dependencies).

## Installation and Setup
Follow these steps to set up the project:

1. Clone the repository:
   ```bash
   git clone https://github.com/oddlyspaced/android-mcp.git
   cd android-mcp
   ```
2. Install the required libraries:
    
    By default this project uses ```uv``` for dependency management, however you can install the required packages via pip if you like.
    ```bash
    uv sync
    ```
    or
    ```bash
    pip install pure-python-adb
    ```

3. Configure the project by editing the `config.py` file to match your ADB setup and device details. (More in next section)
4. Run ```doctor.py``` to ensure that the setup is done correctly.

    Here is reference response from the ```doctor.py``` script :
    ```
    Checking device connection using the following configuration:
    ADB Client Host: 127.0.0.1
    ADB Client Port: 5037
    ADB Device Serial: 32241FDH3002EH

    Device connected: 32241FDH3002EH
    Hello from Android! Ready to use with MCP.
    ``` 

## Configuration Overview
The `config.py` file contains the following configuration options:

- `adb_client_host`: The host address of the ADB server (default: `127.0.0.1`).
- `adb_client_port`: The port of the ADB server (default: `5037`).
- `adb_device_serial`: The serial number or IP address of the connected device. If not specified, the first available device will be used.

## Usage via Claude MCP Config JSON
To use the MCP server, you can interact with it via Claude Desktop MCP configuration JSON. 

The Claude Desktop configuration file is present at the following locations:

    Windows: %APPDATA%\Claude\claude_desktop_config.json
    
    macOS: ~/Library/Application Support/Claude/claude_desktop_config.json

Here is an example configuration using ```uv```:


```json
{
  "mcpServers": {
    "Android MCP": {
      "command": "uv",
      "args": [
        "--directory",
        "/Users/hardik/Projects/Android-Agents/android-mcp", // Replace this with your folder path
        "run",
        "server.py"
      ]
    }
  }
}
```
or with python
```json
{
  "mcpServers": {
    "Android MCP": {
      "command": "python",
      "args": [
        "/Users/hardik/Projects/Android-Agents/android-mcp/server.py", // Replace this with your folder path
      ]
    }
  }
}
```

Alternatively, you can run the MCP server using the following command:
```bash
python server.py
```


## Known Issues
After continously querying the user interface, results might become unavailable temporarily unless device is restarted. This is an issue with dumping the current UI tree. Logic will be updated to fix this shortly.

