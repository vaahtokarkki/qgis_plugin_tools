from typing import Dict, List

from PyQt5.QtCore import QObject
from qgis.core import Qgis


class MockMessageBar(QObject):
    def __init__(self) -> None:
        self.messages: Dict[int, List[str]] = {
            Qgis.Info: [],
            Qgis.Warning: [],
            Qgis.Critical: [],
            Qgis.Success: [],
        }

    def get_messages(self, level: int) -> List[str]:
        """Used to test which messages have been logged"""
        return self.messages[level]

    def pushMessage(self, title, text, level, duration):  # noqa N802
        msg = f"{title}:{text}"
        self.messages[level].append(msg)


class MainWindow(QObject):
    def blockSignals(self, *args):  # noqa N802
        pass
