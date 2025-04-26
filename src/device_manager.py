from config import AndroidMCPConfig
from src.device_handler import DeviceHandler
from ppadb.client import Client as AdbClient


# wrapper class that references the config to create the device object, and also handle scenarios where a device would not be connected
class DeviceManager:
    def __init__(self, config: AndroidMCPConfig):
        self.device = self._initialize_device(config)
        if self.device:
            self.handler = DeviceHandler(self.device)
        else:
            self.handler = None

    def _initialize_device(self, config: AndroidMCPConfig):
        client = AdbClient(host=config.adb_client_host, port=config.adb_client_port)
        try:
            if config.adb_device_serial:
                device = client.device(config.adb_device_serial)
            else:
                device = client.devices()[0]
            return device
        except Exception as e:
            print(f"Failed to initialize connected device: {e}")
            return None

    def __getattr__(self, name):
        if not self.handler:

            def device_not_connected(*args, **kwargs):
                return f"Unable to execute {name}! Device is not connected!"

            return device_not_connected

        attr = getattr(self.handler, name, None)
        if attr is None:
            raise AttributeError(f"'DeviceHandler' object has no attribute '{name}'")
        return attr
