from ppadb.device import Device


class FileHandler:
    def __init__(self, device: Device):
        self.device = device

    def pull(self, remote, local):
        return self.device.pull(remote, local)

    def push(self, local, remote):
        return self.device.push(local, remote)
