from ppadb.device import Device
import xml.etree.ElementTree as ET

from config import AndroidMCPConfig


class UIHandler:
    def __init__(self, device: Device):
        self.device = device

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
