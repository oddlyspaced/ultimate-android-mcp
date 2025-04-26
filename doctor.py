from ppadb.client import Client as AdbClient
from config import AndroidMCPConfig


def check_device_connection():
    # Read configuration
    config = AndroidMCPConfig()
    print("Checking device connection using the following configuration:")

    # Check and print ADB Client Host
    if hasattr(config, "adb_client_host") and config.adb_client_host:
        print(f"ADB Client Host: {config.adb_client_host}")
    else:
        print(
            "! Host variable not present in config, will use pure python adb default."
        )
        config.adb_client_host = "127.0.0.1"  # Default value

    # Check and print ADB Client Port
    if hasattr(config, "adb_client_port") and config.adb_client_port:
        print(f"ADB Client Port: {config.adb_client_port}")
    else:
        print(
            "! Port variable not present in config, will use pure python adb default."
        )
        config.adb_client_port = 5037  # Default value

    # Check and print ADB Client Port
    if hasattr(config, "adb_device_serial") and config.adb_device_serial:
        print(f"ADB Device Serial: {config.adb_device_serial}")
    else:
        print("! Device Serial not specified, will use first available device.")
        config.adb_device_serial = None

    print()
    # Initialize ADB client
    client = AdbClient(host=config.adb_client_host, port=config.adb_client_port)

    try:
        # Check if a specific device is configured
        if config.adb_device_serial:
            device = client.device(config.adb_device_serial)
            if device:
                print(f"Device connected: {device.get_serial_no()}")
                print(device.shell('echo "Hello from Android! Ready to use with MCP."'))
            else:
                print("No device found with the specified serial number!")
        else:
            devices = client.devices()
            if devices:
                print(f"Using the first available device: {devices[0].get_serial_no()}")
                print(
                    devices[0].shell(
                        'echo "Hello from Android! Ready to use with MCP."'
                    )
                )
            else:
                print("No devices are connected.")
    except Exception as e:
        print(f"An error occurred while checking device connection: {e}")


if __name__ == "__main__":
    check_device_connection()
