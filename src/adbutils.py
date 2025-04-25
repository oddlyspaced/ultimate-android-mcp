from .adbexec import run_adb_command


def get_all_packages(
    user_installed_only: bool = False, system_installed_only: bool = False
):
    command = "pm list packages"
    if user_installed_only == True:
        command += " -3"
    if system_installed_only == True:
        command += " -s"
    return [pkg.strip()[8:] for pkg in run_adb_command(command).splitlines()]


def get_system_packages():
    return get_all_packages(system_installed_only=True)


def get_user_packages():
    return get_all_packages(user_installed_only=True)
