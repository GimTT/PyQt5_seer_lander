# IMPORT PACKAGES START
import os

from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import QMainWindow, QDesktopWidget
import seer_lander_ui_free_pack


# IMPORT PACKAGES END

class SeerFreeKnapsackUi(QMainWindow, seer_lander_ui_free_pack.Ui_SeerFreeKnapsack):
    signal_pack_2_lander = pyqtSignal(int)

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setFixedSize(self.width(), self.height())
        self.setWindowTitle("GimTT-FREE-KNAPSACK")

        self.packGenie_list = []

        self.packGenie_view_list = [self.packgenie1, self.packgenie2, self.packgenie3, self.packgenie4,
                                    self.packgenie5, self.packgenie6, self.packgenie7, self.packgenie8,
                                    self.packgenie9, self.packgenie10, self.packgenie11, self.packgenie12]


        # 读入数据
        self.read_knapsack_file_2_list()

        # 背包1
        self.packbuttonq.clicked.connect(self.change_pack)
        self.packbuttonc.clicked.connect(self.change_pack_list)


    # 函数功能：移动窗口至合适位置
    def pack_view_move(self):
        # 屏幕坐标系
        screen = QDesktopWidget().screenGeometry()
        # 窗口坐标系
        size = self.geometry()
        top = (screen.height() - size.height()) / 2.5
        left = (screen.width() - size.width()) / 32
        self.move(left, top)

    # 列表导入到对象
    def read_knapsack_file_2_list(self):
        # 读入自动确认的列表 （自动确认部分应放在dm绑定成功之后）
        try:
            knapsack_list_file = open(os.getcwd() + '\\ini' + "\\knapsack1.txt", "rb")
            for file_name_index in knapsack_list_file:
                self.packGenie_list.append(file_name_index.decode("gb2312").replace("\n", "").replace("\r", ""))
            knapsack_list_file.close()

            for i in range(12):
                if len(self.packGenie_list) > i:
                    self.packGenie_view_list[i].setText(self.packGenie_list[i])

        except:
            # pass
            print('打开文件流错误')

        return 0

    # 背包更换
    def change_pack(self):
        self.signal_pack_2_lander.emit(7)

    # 背包列表更换
    def change_pack_list(self):
        knapsack_list_file = open(os.getcwd() + '\\ini' + "\\knapsack1.txt", "w")
        for i in range(12):
            if self.packGenie_view_list[i].text() != '':
                knapsack_list_file.write(self.packGenie_view_list[i].text() + '\n')
        knapsack_list_file.close()


