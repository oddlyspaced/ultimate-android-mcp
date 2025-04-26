from ppadb.device import Device


class InputHandler:
    def __init__(self, device: Device):
        self.device = device

    def input_keyevent(self, keycode):
        return self.device.input_keyevent(keycode)

    def input_back(self):
        return self.device.input_keyevent("KEYCODE_BACK")

    def input_home(self):
        return self.device.input_keyevent("KEYCODE_HOME")

    def input_tap(self, x, y):
        return self.device.input_tap(x, y)

    def input_text(self, text):
        return self.device.input_text(text)

    def input_press(self, keycode):
        return self.device.input_press(keycode)

    def input_roll(self, dx, dy):
        return self.device.input_roll(dx, dy)

    def input_swipe(self, x1, y1, x2, y2, duration_ms=None):
        return self.device.input_swipe(x1, y1, x2, y2, duration_ms)

    def is_keyboard_open(self) -> bool:
        # adb shell dumpsys input_method | grep mInputShown
        return "true" in self.device.shell("dumpsys input_method | grep mInputShown")
