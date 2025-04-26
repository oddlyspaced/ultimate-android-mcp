from ppadb.device import Device


# device specific information
class DeviceInfoHandler:
    def __init__(self, device: Device):
        self.device = device

    # returns the serial number of the device
    def get_serial_no(self):
        return self.device.get_serial_no()

    # returns build.prop properties
    def get_properties(self):
        return self.device.get_properties()

    # returns device overlay config properties
    def list_features(self):
        return self.device.list_features()

    # returns the device battery level
    def get_battery_level(self):
        return self.device.get_battery_level()

    def wm_density(self):
        return self.device.wm_density()

    def wm_size(self):
        return self.device.wm_size()
