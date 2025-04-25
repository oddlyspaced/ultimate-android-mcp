from ppadb.device import Device


# wrapper class to execute functions over the connected device
class DeviceHandler:
    def __init__(self, device: Device):
        self.device = device

    def get_all_packages(
        self, user_installed_only: bool = False, system_installed_only: bool = False
    ):
        command = "pm list packages"
        if user_installed_only == True:
            command += " -3"
        if system_installed_only == True:
            command += " -s"
        return [pkg.strip()[8:] for pkg in self.device.shell(command).splitlines()]

    def get_system_packages(self):
        return self.get_all_packages(system_installed_only=True)

    def get_user_packages(self):
        return self.get_all_packages(user_installed_only=True)
