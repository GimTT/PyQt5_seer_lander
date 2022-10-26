# IMPORT PACKAGES START
from PyQt5 import QtWidgets
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import QMainWindow, QDesktopWidget
# IMPORT PACKAGES END

# IMPORT USER PY FILE START
import seer_lander_ui_auto


# IMPORT USER PY FILE END

class AutoUi(QMainWindow, seer_lander_ui_auto.Ui_autoWindow):
    signal_auto_2_lander = pyqtSignal(int)

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.point = None
        self.genie = None
        self.setFixedSize(self.width(), self.height())

    # 函数功能：移动窗口
    def auto_view_move(self):
        # 屏幕坐标系
        screen = QDesktopWidget().screenGeometry()
        # 窗口坐标系
        size = self.geometry()
        top = (screen.height() - size.height()) / 12
        left = (screen.width() - size.width()) / 2
        self.move(left, top)
        self.GuanQiaXuanZe_pushButton.clicked.connect(self.check_point)
        self.GuanQiaQueRen_pushButton.clicked.connect(self.auto_fight_begin)

        self.JingLingXuanZe_pushButton.clicked.connect(self.check_genie)
        self.JingLingQueRen_pushButton.clicked.connect(self.auto_genie_begin)

    def check_point(self):
        self.point = QtWidgets.QFileDialog.getExistingDirectory(None, "选取文件夹", "./")  # 起始路径
        self.label_GuanQiaPeiZhi.setText(self.point)

    def check_genie(self):
        self.genie = QtWidgets.QFileDialog.getExistingDirectory(None, "选取文件夹", "./")  # 起始路径
        self.label_JingLingPeiZhi.setText(self.genie)

    def auto_fight_begin(self):
        self.signal_auto_2_lander.emit(5)

    def auto_genie_begin(self):
        self.signal_auto_2_lander.emit(5)
