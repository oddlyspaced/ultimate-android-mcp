from ppadb.device import Device


class ShellHandler:
    def __init__(self, device: Device):
        self.device = device

    def shell(self, command):
        return self.device.shell(command)
