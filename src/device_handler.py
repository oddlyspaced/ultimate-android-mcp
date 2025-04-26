from ppadb.device import Device
import xml.etree.ElementTree as ET


# wrapper class to execute functions over the connected device
class DeviceHandler:
    def __init__(self, device: Device):
        self.device = device

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

    def get_current_ui_labels(self):
        self.device.shell("uiautomator dump")
        self.device.pull("/sdcard/window_dump.xml", "window_dump.xml")
        self.device.shell("rm /sdcard/window_dump.xml")

        tree = ET.parse("window_dump.xml")
        root = tree.getroot()
        results = []

        attributes_to_extract = [
            "text",
            "bounds",
            "content-desc",
            "checkable",
            "checked",
            "clickable",
            "enabled",
            "focusable",
            "focused",
            "long-clickable",
            "password",
            "selected",
            "hint",
        ]

        for node in root.iter("node"):
            text = node.attrib.get("text", "").strip()
            content_desc = node.attrib.get("content-desc", "").strip()
            if text or content_desc:
                element = {
                    attr: node.attrib.get(attr, "") for attr in attributes_to_extract
                }
                results.append(element)

        return results

    def get_current_focused_nodes(self):
        self.device.shell("uiautomator dump")
        self.device.pull("/sdcard/window_dump.xml", "window_dump.xml")
        self.device.shell("rm /sdcard/window_dump.xml")

        tree = ET.parse("window_dump.xml")
        root = tree.getroot()

        for node in root.iter("node"):
            if node.attrib.get("focused") == "true":
                return node.attrib

        return None

    # def get_clickable_nodes(self):
    #     self.device.shell("uiautomator dump")
    #     self.device.pull("/sdcard/window_dump.xml", "window_dump.xml")
    #     self.device.shell("rm /sdcard/window_dump.xml")

    #     tree = ET.parse("window_dump.xml")
    #     root = tree.getroot()
    #     clickable_nodes = []

    #     for node in root.iter("node"):
    #         if node.attrib.get("clickable") == "true":
    #             clickable_nodes.append(node.attrib)

    #     return clickable_nodes

    def is_keyboard_open(self) -> bool:
        # adb shell dumpsys input_method | grep mInputShown
        return "true" in self.device.shell("dumpsys input_method | grep mInputShown")

    def input_tap(self, x: int, y: int):
        self.device.shell(f"input tap {x} {y}")

    def input_text(self, text: str):
        self.device.shell(f"input text {text.replace(' ', '%s')}")

    def execute_adb_shell(self, command: str):
        return self.device.shell(command)
