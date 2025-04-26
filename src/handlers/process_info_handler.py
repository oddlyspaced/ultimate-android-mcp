from ppadb.device import Device


class ProcessInfoHandler:
    def __init__(self, device: Device):
        self.device = device

    # returns the pid for a given package name
    def get_pid(self, package_name):
        return self.device.get_pid(package_name)

    # returns the activies currently on top
    def get_top_activities(self):
        return self.device.get_top_activities()

    # returns the singular activity currently on top
    def get_top_activity(self):
        return self.device.get_top_activity()
