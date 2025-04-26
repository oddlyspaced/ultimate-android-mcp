from config import AndroidMCPConfig
from ppadb.client import Client as AdbClient

from src.handlers.cpu_info_handler import CpuInfoHandler
from src.handlers.device_info_handler import DeviceInfoHandler
from src.handlers.file_handler import FileHandler
from src.handlers.input_handler import InputHandler
from src.handlers.package_handler import PackageHandler
from src.handlers.process_info_handler import ProcessInfoHandler
from src.handlers.shell_handler import ShellHandler
from src.handlers.ui_handler import UIHandler


# wrapper class that references the config to create the device object, and also handle scenarios where a device would not be connected
class DeviceManager:
    def __init__(self, config: AndroidMCPConfig):
        self.device = self._initialize_device(config)
        if self.device:
            self.cpu_info = CpuInfoHandler(self.device)
            self.device_info = DeviceInfoHandler(self.device)
            self.file = FileHandler(self.device)
            self.input = InputHandler(self.device)
            self.package = PackageHandler(self.device)
            self.process_info = ProcessInfoHandler(self.device)
            self.shell = ShellHandler(self.device)
            self.ui = UIHandler(self.device, config)

        else:
            self.cpu_info = None
            self.device_info = None
            self.file = None
            self.input = None
            self.package = None
            self.process_info = None
            self.shell = None
            self.ui = None

    def _initialize_device(self, config: AndroidMCPConfig):
        # sanitsize config object
        if hasattr(config, "adb_client_host") == False:
            config.adb_client_host = "127.0.0.1"
        if hasattr(config, "adb_client_port") == False:
            config.adb_client_port = 5037
        if hasattr(config, "adb_device_serial") == False:
            config.adb_device_serial = None

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
        if not self.device:

            def device_not_connected(*args, **kwargs):
                return f"Unable to execute {name}! Device is not connected!"

            return device_not_connected

        # Search for the attribute across all handler objects
        for handler in [
            self.cpu_info,
            self.device_info,
            self.file,
            self.input,
            self.package,
            self.process_info,
            self.shell,
            self.ui,
        ]:
            if handler and hasattr(handler, name):
                return getattr(handler, name)

        raise AttributeError(f"'DeviceManager' object has no attribute '{name}'")
