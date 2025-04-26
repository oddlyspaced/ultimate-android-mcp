from ppadb.device import Device


class PackageHandler:
    def __init__(self, device: Device):
        self.device = device

    def install(self, apk_path):
        return self.device.install(apk_path)

    def uninstall(self, package_name):
        return self.device.uninstall(package_name)

    def is_installed(self, package_name):
        return self.device.is_installed(package_name)

    def get_all_packages(
        self, user_installed_only: bool = False, system_installed_only: bool = False
    ) -> list[str]:
        command = "pm list packages"
        if user_installed_only == True:
            command += " -3"
        if system_installed_only == True:
            command += " -s"
        return [pkg.strip()[8:] for pkg in self.device.shell(command).splitlines()]

    def get_system_packages(self) -> list[str]:
        return self.get_all_packages(system_installed_only=True)

    def get_user_packages(self) -> list[str]:
        return self.get_all_packages(user_installed_only=True)

    def launch_app(self, package_name: str):
        # adb shell monkey -p com.example.app -c android.intent.category.LAUNCHER 1
        return self.device.shell(
            f"monkey -p {package_name} -c android.intent.category.LAUNCHER 1"
        )
