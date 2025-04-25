import subprocess


# runs a command as -> adb shell $command
def run_adb_command(command: str):
    process = subprocess.Popen(
        ["adb", "shell", command], stdout=subprocess.PIPE, stderr=subprocess.PIPE
    )
    stdout, stderr = process.communicate()
    if process.returncode != 0:
        print("----- Error executing adb shell command")
        print(stderr.decode())
        print("----- ")
        raise Exception(f"Error executing adb shell command: {command}")
    else:
        return stdout.decode()
