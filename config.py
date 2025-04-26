class AndroidMCPConfig:
    adb_client_host = "127.0.0.1"  # adb server host url
    adb_client_port = 5037  # adb server host port
    # serial number or ip of the connected device to use, if this is not present the first available device would be used
    adb_device_serial = "32241FDH3002EH"
    # adb_device_serial = "172.20.0.1:5555"
    device_temp_folder = "/sdcard/.androidmcp"
