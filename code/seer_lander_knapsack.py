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

        self.pack1genie_list = []
        self.pack2genie_list = []
        self.pack3genie_list = []
        self.pack4genie_list = []
        self.pack5genie_list = []
        self.pack6genie_list = []

        self.pack1genie_view_list = [self.pack1genie1, self.pack1genie2, self.pack1genie3, self.pack1genie4,
                                     self.pack1genie5, self.pack1genie6, self.pack1genie7, self.pack1genie8,
                                     self.pack1genie9, self.pack1genie10, self.pack1genie11, self.pack1genie12]
        self.pack2genie_view_list = [self.pack2genie1, self.pack2genie2, self.pack2genie3, self.pack2genie4,
                                     self.pack2genie5, self.pack2genie6, self.pack2genie7, self.pack2genie8,
                                     self.pack2genie9, self.pack2genie10, self.pack2genie11, self.pack2genie12]
        self.pack3genie_view_list = [self.pack3genie1, self.pack3genie2, self.pack3genie3, self.pack3genie4,
                                     self.pack3genie5, self.pack3genie6, self.pack3genie7, self.pack3genie8,
                                     self.pack3genie9, self.pack3genie10, self.pack3genie11, self.pack3genie12]
        self.pack4genie_view_list = [self.pack4genie1, self.pack4genie2, self.pack4genie3, self.pack4genie4,
                                     self.pack4genie5, self.pack4genie6, self.pack4genie7, self.pack4genie8,
                                     self.pack4genie9, self.pack4genie10, self.pack4genie11, self.pack4genie12]
        self.pack5genie_view_list = [self.pack5genie1, self.pack5genie2, self.pack5genie3, self.pack5genie4,
                                     self.pack5genie5, self.pack5genie6, self.pack5genie7, self.pack5genie8,
                                     self.pack5genie9, self.pack5genie10, self.pack5genie11, self.pack5genie12]
        self.pack6genie_view_list = [self.pack6genie1, self.pack6genie2, self.pack6genie3, self.pack6genie4,
                                     self.pack6genie5, self.pack6genie6, self.pack6genie7, self.pack6genie8,
                                     self.pack6genie9, self.pack6genie10, self.pack6genie11, self.pack6genie12]

        # 读入数据
        self.read_knapsack_file_2_list()

        # 背包1
        self.pack1button1q.clicked.connect(self.change_pack1)
        self.pack1button2c.clicked.connect(self.change_pack1_list)

        # 背包2
        self.pack2button1q.clicked.connect(self.change_pack2)
        self.pack2button2c.clicked.connect(self.change_pack2_list)

        # 背包3
        self.pack3button1q.clicked.connect(self.change_pack3)
        self.pack3button2c.clicked.connect(self.change_pack3_list)

        # 背包4
        self.pack4button1q.clicked.connect(self.change_pack4)
        self.pack4button2c.clicked.connect(self.change_pack4_list)

        # 背包5
        self.pack5button1q.clicked.connect(self.change_pack5)
        self.pack5button2c.clicked.connect(self.change_pack5_list)

        # 背包6
        self.pack6button1q.clicked.connect(self.change_pack6)
        self.pack6button2c.clicked.connect(self.change_pack6_list)

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
                self.pack1genie_list.append(file_name_index.decode("gb2312").replace("\n", "").replace("\r", ""))
            knapsack_list_file.close()

            knapsack_list_file = open(os.getcwd() + '\\ini' + "\\knapsack2.txt", "rb")
            for file_name_index in knapsack_list_file:
                self.pack2genie_list.append(file_name_index.decode("gb2312").replace("\n", "").replace("\r", ""))
            knapsack_list_file.close()

            knapsack_list_file = open(os.getcwd() + '\\ini' + "\\knapsack3.txt", "rb")
            for file_name_index in knapsack_list_file:
                self.pack3genie_list.append(file_name_index.decode("gb2312").replace("\n", "").replace("\r", ""))
            knapsack_list_file.close()

            knapsack_list_file = open(os.getcwd() + '\\ini' + "\\knapsack4.txt", "rb")
            for file_name_index in knapsack_list_file:
                self.pack4genie_list.append(file_name_index.decode("gb2312").replace("\n", "").replace("\r", ""))
            knapsack_list_file.close()

            knapsack_list_file = open(os.getcwd() + '\\ini' + "\\knapsack5.txt", "rb")
            for file_name_index in knapsack_list_file:
                self.pack5genie_list.append(file_name_index.decode("gb2312").replace("\n", "").replace("\r", ""))
            knapsack_list_file.close()

            knapsack_list_file = open(os.getcwd() + '\\ini' + "\\knapsack6.txt", "rb")
            for file_name_index in knapsack_list_file:
                self.pack6genie_list.append(file_name_index.decode("gb2312").replace("\n", "").replace("\r", ""))
            knapsack_list_file.close()

            for i in range(12):
                if len(self.pack1genie_list) > i:
                    self.pack1genie_view_list[i].setText(self.pack1genie_list[i])
                if len(self.pack2genie_list) > i:
                    self.pack2genie_view_list[i].setText(self.pack2genie_list[i])
                if len(self.pack3genie_list) > i:
                    self.pack3genie_view_list[i].setText(self.pack3genie_list[i])
                if len(self.pack4genie_list) > i:
                    self.pack4genie_view_list[i].setText(self.pack4genie_list[i])
                if len(self.pack5genie_list) > i:
                    self.pack5genie_view_list[i].setText(self.pack5genie_list[i])
                if len(self.pack6genie_list) > i:
                    self.pack6genie_view_list[i].setText(self.pack6genie_list[i])

        except:
            # pass
            print('打开文件流错误')

        return 0

    # 背包更换
    def change_pack1(self):
        self.signal_pack_2_lander.emit(7)

    # 背包列表更换
    def change_pack1_list(self):
        knapsack_list_file = open(os.getcwd() + '\\ini' + "\\knapsack1.txt", "w")
        for i in range(12):
            if self.pack1genie_view_list[i].text() != '':
                knapsack_list_file.write(self.pack1genie_view_list[i].text() + '\n')
        knapsack_list_file.close()

    # 背包更换
    def change_pack2(self):
        self.signal_pack_2_lander.emit(8)

    # 背包列表更换
    def change_pack2_list(self):
        knapsack_list_file = open(os.getcwd() + '\\ini' + "\\knapsack2.txt", "w")
        for i in range(12):
            if self.pack2genie_view_list[i].text() != '':
                knapsack_list_file.write(self.pack2genie_view_list[i].text() + '\n')
        knapsack_list_file.close()

    # 背包更换
    def change_pack3(self):
        self.signal_pack_2_lander.emit(9)

    # 背包列表更换
    def change_pack3_list(self):
        knapsack_list_file = open(os.getcwd() + '\\ini' + "\\knapsack3.txt", "w")
        for i in range(12):
            if self.pack3genie_view_list[i].text() != '':
                knapsack_list_file.write(self.pack3genie_view_list[i].text() + '\n')
        knapsack_list_file.close()

    # 背包更换
    def change_pack4(self):
        self.signal_pack_2_lander.emit(10)

    # 背包列表更换
    def change_pack4_list(self):
        knapsack_list_file = open(os.getcwd() + '\\ini' + "\\knapsack4.txt", "w")
        for i in range(12):
            if self.pack4genie_view_list[i].text() != '':
                knapsack_list_file.write(self.pack4genie_view_list[i].text() + '\n')
        knapsack_list_file.close()

    # 背包更换
    def change_pack5(self):
        self.signal_pack_2_lander.emit(11)

    # 背包列表更换
    def change_pack5_list(self):
        knapsack_list_file = open(os.getcwd() + '\\ini' + "\\knapsack5.txt", "w")
        for i in range(12):
            if self.pack5genie_view_list[i].text() != '':
                knapsack_list_file.write(self.pack5genie_view_list[i].text() + '\n')
        knapsack_list_file.close()

    # 背包更换
    def change_pack6(self):
        self.signal_pack_2_lander.emit(12)

    # 背包列表更换
    def change_pack6_list(self):
        knapsack_list_file = open(os.getcwd() + '\\ini' + "\\knapsack6.txt", "w")
        for i in range(12):
            if self.pack6genie_view_list[i].text() != '':
                knapsack_list_file.write(self.pack6genie_view_list[i].text() + '\n')
        knapsack_list_file.close()

