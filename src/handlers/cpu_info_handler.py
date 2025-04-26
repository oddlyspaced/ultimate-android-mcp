from ppadb.device import Device


class CpuInfoHandler:
    def __init__(self, device: Device):
        self.device = device

    # returns count of cpu cores
    def cpu_count(self):
        return self.device.cpu_count()

    # retuns the current cpu load
    def cpu_percent(self):
        return self.device.cpu_percent()
