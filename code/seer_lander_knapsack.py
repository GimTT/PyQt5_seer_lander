# IMPORT PACKAGES START
import os

from PyQt5.QtCore import pyqtSignal
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QMainWindow, QDesktopWidget
import seer_lander_ui_free_pack


# IMPORT PACKAGES END

class SeerFreeKnapsackUi(QMainWindow, seer_lander_ui_free_pack.Ui_SeerFreeKnapsack):
    signal_pack_2_lander = pyqtSignal(int)

    def __init__(self):
        super().__init__()

        # 设置图标
        self.setWindowIcon(QIcon('./ini/GimTT_Lander_img.ico'))

        self.setupUi(self)
        self.pack_filename = 'knapsack1.txt'
        self.pack_title_filename = 'knapsack1_title.txt'
        self.setFixedSize(self.width(), self.height())
        self.setWindowTitle("GimTT-FREE-KNAPSACK")

        # 下拉列表:add

        self.packswitch_combox.addItems(['1', '2', '3', '4', '5', '6'])
        self.packswitch_combox.currentIndexChanged[str].connect(self.switch_genie_pack)

        # 精灵的列表缓冲区
        self.packGenie_list = []
        self.packGenie_view_list = [self.packgenie1, self.packgenie2, self.packgenie3, self.packgenie4,
                                    self.packgenie5, self.packgenie6, self.packgenie7, self.packgenie8,
                                    self.packgenie9, self.packgenie10, self.packgenie11, self.packgenie12]

        # 读入数据
        self.read_knapsack_file_2_list()

        # 背包1
        self.packbuttonq.clicked.connect(self.change_pack)
        self.packbuttonc.clicked.connect(self.change_pack_list)

    # 函数功能：切换到指定背包
    def switch_genie_pack(self, pack_index):
        if pack_index == '1':
            self.pack_filename = 'knapsack1.txt'
            self.pack_title_filename = 'knapsack1_title.txt'
        elif pack_index == '2':
            self.pack_filename = 'knapsack2.txt'
            self.pack_title_filename = 'knapsack2_title.txt'
        elif pack_index == '3':
            self.pack_filename = 'knapsack3.txt'
            self.pack_title_filename = 'knapsack3_title.txt'
        elif pack_index == '4':
            self.pack_filename = 'knapsack4.txt'
            self.pack_title_filename = 'knapsack4_title.txt'
        elif pack_index == '5':
            self.pack_filename = 'knapsack5.txt'
            self.pack_title_filename = 'knapsack5_title.txt'
        elif pack_index == '6':
            self.pack_filename = 'knapsack6.txt'
            self.pack_title_filename = 'knapsack6_title.txt'
        self.clear_pack_text()
        self.read_knapsack_file_2_list()

    # 函数功能：移动窗口至合适位置
    def pack_view_move(self):
        # 屏幕坐标系
        screen = QDesktopWidget().screenGeometry()
        # 窗口坐标系
        size = self.geometry()
        top = (screen.height() - size.height()) / 4.7
        left = (screen.width() - size.width()) / 14 * 13
        self.move(left, top)

    # 列表导入到对象
    def read_knapsack_file_2_list(self):
        # 读入自动确认的列表 （自动确认部分应放在dm绑定成功之后）
        self.packGenie_list = []
        try:
            knapsack_list_file = open(os.getcwd() + '\\ini' + "\\" + self.pack_filename, "rb")
            for file_name_index in knapsack_list_file:
                self.packGenie_list.append(file_name_index.decode("gb2312").replace("\n", "").replace("\r", ""))
            knapsack_list_file.close()

            knapsack_title_file = open(os.getcwd() + '\\ini' + "\\" + self.pack_title_filename, "rb")
            self.packtitle.setText(knapsack_title_file.read().decode("gb2312").replace("\n", "").replace("\r", ""))
            knapsack_title_file.close()

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
        knapsack_list_file = open(os.getcwd() + '\\ini' + "\\" + self.pack_filename, "w")
        for i in range(12):
            if self.packGenie_view_list[i].text() != '':
                knapsack_list_file.write(self.packGenie_view_list[i].text() + '\n')
        knapsack_list_file.close()

        knapsack_title_file = open(os.getcwd() + '\\ini' + "\\" + self.pack_title_filename, "w")
        knapsack_title_file.write(self.packtitle.text() + '\n')
        knapsack_title_file.close()

    # 函数功能：清除文本
    def clear_pack_text(self):
        for i in range(12):
            self.packGenie_view_list[i].setText('')

        self.packtitle.setText('')
