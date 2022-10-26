# IMPORT PACKAGES START
from ctypes import CDLL, c_float
from PyQt5.QtWidgets import QMainWindow, QDesktopWidget
import seer_lander_ui_speed


# IMPORT PACKAGES END

class SpeedUi(QMainWindow, seer_lander_ui_speed.Ui_SpeedWindow):

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setFixedSize(self.width(), self.height())

        # 载入变速dll
        self.lib = CDLL(r"SpeedControl.dll")

        self.setWindowTitle("GimTT-SPEED-Ctrler")

        self.textEdit_speed.setText("1")
        self.horizontalSlider.setMinimum(1)
        self.horizontalSlider.setMaximum(4)
        self.horizontalSlider.setSingleStep(1)
        self.horizontalSlider.valueChanged.connect(self.speed_text_change)

        self.pushButton_HuiFu.clicked.connect(self.speed_text_clear)
        self.pushButton_QueRen.clicked.connect(self.speed_change)

    def speed_text_change(self):
        self.textEdit_speed.setText("%s" % self.horizontalSlider.value())

    def speed_text_clear(self):
        self.textEdit_speed.setText("1")
        self.horizontalSlider.setValue(1)
        self.lib.SetRange(c_float(float(1)))

    def speed_change(self):
        value = self.textEdit_speed.toPlainText()
        self.lib.SetRange(c_float(float(value)))

    def speed_view_move(self):
        # 屏幕坐标系
        screen = QDesktopWidget().screenGeometry()
        # 窗口坐标系
        size = self.geometry()
        top = (screen.height() - size.height()) / 10 * 8.5
        left = (screen.width() - size.width()) / 2
        self.move(left, top)
