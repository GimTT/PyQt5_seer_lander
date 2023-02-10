from PyQt5.QtCore import QThread
from PyQt5.QtWidgets import QApplication

GAME_INIT_WIDTH = 960
GAME_INIT_HEIGHT = 560


class GameWindowThread(QThread):

    def __init__(self, show_area):
        super().__init__()
        self.disp_area = show_area
        self.zoom_scale = 100
        self.normal_scale = 100
        self.desktop = QApplication.desktop()
        self.disp_area.setControl("{8856F961-340A-11D0-A96B-00C04FD705A2}")
        self.disp_area.setProperty("DisplayAlerts", False)
        self.disp_area.setProperty("DisplayScrollBars", True)
        self.disp_area.dynamicCall("Navigate(const QString&)", "http://seer.61.com/play.shtml")
        # 公司防查
        # self.game_area.dynamicCall("Navigate(const QString&)", "www.baidu.com")

    # name      :   refresh
    # parameter :   none
    # function  :   刷新页面
    def refresh(self):
        self.disp_area.dynamicCall("Refresh()")

    # name      :   set_size
    # parameter :   scale:要放大到的比例
    # function  :   通过调用ie的缩放函数放大窗口
    def set_size(self, scale):
        self.zoom_scale = scale
        self.disp_area.dynamicCall(
            "ExecWB(OLECMDID_OPTICAL_ZOOM, OLECMDEXECOPT_DODEFAULT, " + str(self.zoom_scale) + ")")

    # name      :   reset_size
    # parameter :   none
    # function  :   重置页面大小
    def reset_size(self):
        self.zoom_scale = self.normal_scale
        self.disp_area.dynamicCall(
            "ExecWB(OLECMDID_OPTICAL_ZOOM, OLECMDEXECOPT_DODEFAULT, " + str(self.zoom_scale) + ")")
