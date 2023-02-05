from PyQt5.QtCore import QThread
from PyQt5.QtWidgets import QApplication

GAME_INIT_WIDTH = 960
GAME_INIT_HEIGHT = 560


class GameWindowThread(QThread):

    def __init__(self, show_area):
        super().__init__()
        self.game_area = show_area
        self.size = 100
        self.game_area.setControl("{8856F961-340A-11D0-A96B-00C04FD705A2}")
        self.game_area.setProperty("DisplayAlerts", False)
        self.game_area.setProperty("DisplayScrollBars", True)
        self.game_area.dynamicCall("Navigate(const QString&)", "http://seer.61.com/play.shtml")

    def refresh(self):
        self.game_area.dynamicCall("Refresh()")
        # self.game_area.dynamicCall("ExecWB(OLECMDID_OPTICAL_ZOOM, OLECMDEXECOPT_DODEFAULT, 150)")

    def size_50percent(self):
        self.size = 50
        self.game_area.dynamicCall("ExecWB(OLECMDID_OPTICAL_ZOOM, OLECMDEXECOPT_DODEFAULT, " + str(self.size) + ")")

    def size_75percent(self):
        self.size = 75
        self.game_area.dynamicCall("ExecWB(OLECMDID_OPTICAL_ZOOM, OLECMDEXECOPT_DODEFAULT, " + str(self.size) + ")")

    def size_125percent(self):
        self.size = 125
        self.game_area.dynamicCall("ExecWB(OLECMDID_OPTICAL_ZOOM, OLECMDEXECOPT_DODEFAULT, " + str(self.size) + ")")

    def size_150percent(self):
        self.size = 150
        self.game_area.dynamicCall("ExecWB(OLECMDID_OPTICAL_ZOOM, OLECMDEXECOPT_DODEFAULT, " + str(self.size) + ")")

    def size_max(self):
        desktop = QApplication.desktop()
        self.size = ((desktop.width() / GAME_INIT_WIDTH) * 100) * 0.9
        self.game_area.dynamicCall("ExecWB(OLECMDID_OPTICAL_ZOOM, OLECMDEXECOPT_DODEFAULT, " + str(int(self.size)) + ")")

    def size_reset(self):
        self.size = 100
        self.game_area.dynamicCall("ExecWB(OLECMDID_OPTICAL_ZOOM, OLECMDEXECOPT_DODEFAULT, " + str(self.size) + ")")
        # self.game_area.dynamicCall(self.sizeConfig(200))
