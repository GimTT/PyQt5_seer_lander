# IMPORT PACKAGES START
import os
import sys
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import pyqtSignal


# IMPORT PACKAGES END


# 配置图片序列以及显示顺序
class Nono:

    def __init__(self):
        self.image_key = 1
        self.codePath = os.getcwd()
        self.nonoConf = open(self.codePath + "\\ini" + "\\nono_config.txt", "r", encoding="gb2312")
        self.nonoName = self.nonoConf.read()
        self.nonoPath = 'nonoImg' + '/' + self.nonoName
        self.nonoList = os.listdir(self.nonoPath)
        self.image_key_max = len(self.nonoList)
        self.image_url = self.nonoPath + '/('
        self.image = self.image_url + str(self.image_key) + ').png'
        self.base_image = 'nonoImg' + '/' + 'nono_img_base.png'
        self.mouse_move_x = None
        self.mouse_move_y = None

    # 函数功能：导入动态序列
    def gif(self):
        if self.image_key < self.image_key_max:
            self.image_key += 1
        else:
            self.image_key = 1
        self.image = self.image_url + str(self.image_key) + ').png'


# 右键菜单以及对应函数
class MyLabel(QLabel):
    signal_nono_2_lander = pyqtSignal(int)

    def __init__(self, *args, **kw):

        super().__init__(*args)

        # 声明
        self.menu = None
        self.music_mute = False
        self.setContextMenuPolicy(Qt.CustomContextMenu)
        # 开放右键策略
        self.customContextMenuRequested.connect(self.right_menu_show)

    # 函数功能：添加右键菜单
    def right_menu_show(self, pos):
        self.menu = QMenu(self)
        self.menu.addAction(QAction('刷新', self, triggered=self.re_fresh))
        self.menu.addAction(QAction('变速', self, triggered=self.set_speed))
        self.menu.addAction(QAction('静音', self, triggered=self.mute_music))
        self.menu.addAction(QAction('背包', self, triggered=self.pack_seer))

        # 脚本合集（期望使用多线程实现）
        script = self.menu.addMenu('脚本')
        script.addAction(QAction('自动八四', self, triggered=self.auto_84))

        # 登陆器nono皮肤
        skin = self.menu.addMenu('皮肤')

        # 精灵王
        skin_genie_king = skin.addMenu('精灵王')
        skin_genie_king.addAction(QAction('火王', self, triggered=self.switch_skin_anes))
        skin_genie_king.addAction(QAction('水王', self, triggered=self.switch_skin_conlan))
        skin_genie_king.addAction(QAction('草王', self, triggered=self.switch_skin_moreer))
        skin_genie_king.addAction(QAction('光王', self, triggered=self.switch_skin_skali))
        skin_genie_king.addAction(QAction('超能王', self, triggered=self.switch_skin_hisev))

        # 大暗黑天
        skin_dark_heaven = skin.addMenu('大暗黑天')
        skin_dark_heaven.addAction(QAction('威斯克', self, triggered=self.switch_skin_vsk))

        # 其他
        skin_other = skin.addMenu('其他')
        skin_other.addAction(QAction('潘多拉', self, triggered=self.switch_skin_pandora))

        self.menu.addAction(QAction('退出', self, triggered=self.quit))
        self.menu.exec_(QCursor.pos())

    # 函数功能：自动84
    def auto_84(self):
        self.signal_nono_2_lander.emit(98)

    # 函数功能：切换皮肤
    def switch_skin_base(self, sequence_name):
        path = os.getcwd()
        nono_conf = open(path + "\\ini" + "\\nono_config.txt", "w", encoding="gb2312")
        nono_conf.write(sequence_name)
        nono_conf.close()
        self.signal_nono_2_lander.emit(99)

    # 函数功能：切火王皮肤
    def switch_skin_anes(self):
        self.switch_skin_base("Aens")

    # 函数功能：切水王皮肤
    def switch_skin_conlan(self):
        self.switch_skin_base("ConLan")

    # 函数功能：切超能王皮肤
    def switch_skin_hisev(self):
        self.switch_skin_base("Hisev")

    # 函数功能：切草王皮肤
    def switch_skin_moreer(self):
        self.switch_skin_base("Moreer")

    # 函数功能：切光王皮肤
    def switch_skin_skali(self):
        self.switch_skin_base("Skali")

    # 函数功能：切潘多拉皮肤
    def switch_skin_pandora(self):
        self.switch_skin_base("Pandora")

    # 函数功能：切威斯克皮肤
    def switch_skin_vsk(self):
        self.switch_skin_base("Vsk")

    # 函数功能：魔法脚本（未实现）
    def seer_magic(self):
        pass

    # 函数功能：退出（通过sys.exit）
    def quit(self):
        self.close()
        sys.exit()

    # 函数功能：发送信号打开背包窗口
    def pack_seer(self):
        self.signal_nono_2_lander.emit(6)

    # 函数功能：发送信号打开脚本窗口
    def auto_seer(self):
        self.signal_nono_2_lander.emit(4)

    # 函数功能：切换静音/声音
    def mute_music(self):
        if not self.music_mute:
            self.signal_nono_2_lander.emit(2)
            self.music_mute = True
        elif self.music_mute:
            self.signal_nono_2_lander.emit(3)
            self.music_mute = False

    # 函数功能：变速
    def set_speed(self):
        self.signal_nono_2_lander.emit(1)

    # 函数功能：刷新
    def re_fresh(self):
        self.signal_nono_2_lander.emit(0)


# 桌宠类
class TablePet(QWidget):

    def __init__(self):
        super(TablePet, self).__init__()

        self.pm_nono = None
        self.lb_nono = None
        self.signal_from_nono = None
        self.nono = Nono()

        self.is_follow_mouse = False

        self.init_ui()

        # 每隔一段时间执行
        timer_nono = QTimer(self)
        timer_nono.timeout.connect(self.gem)
        timer_nono.start(100)

    # 函数功能：执行gif
    def gem(self):
        # 僵尸实现gif效果
        self.nono.gif()
        self.pm_nono = QPixmap(self.nono.image)
        self.lb_nono.setPixmap(self.pm_nono)

    # 函数功能：载入ui
    def init_ui(self):

        # 屏幕大小
        screen = QDesktopWidget().screenGeometry()
        self.setGeometry(0, 0, screen.width(), screen.height())

        # 僵尸标签
        self.lb_nono = MyLabel(self)
        self.pm_nono = QPixmap(self.nono.image)
        self.lb_nono.setPixmap(self.pm_nono)

        # 窗口坐标系
        size = self.lb_nono.geometry()
        top = (screen.height() - size.height()) / 10 * 6
        left = (screen.width() - size.width()) / 6 * 5
        self.lb_nono.move(left, top)

        self.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint | Qt.SubWindow)
        self.setAutoFillBackground(False)
        self.setAttribute(Qt.WA_TranslucentBackground, True)
        self.showMaximized()

    # 函数功能：双击对应事件
    def mouseDoubleClickEvent(self, QMouseEvent):
        pass

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.is_follow_mouse = True

            event.accept()
            self.setCursor(QCursor(Qt.OpenHandCursor))

    def mouseMoveEvent(self, event):
        if Qt.LeftButton and self.is_follow_mouse:
            self.nono.mouse_move_x = QCursor.pos().x() - 129  # nono图片大小258*240
            self.nono.mouse_move_y = QCursor.pos().y() - 120
            self.lb_nono.move(self.nono.mouse_move_x, self.nono.mouse_move_y)
            event.accept()

    def mouseReleaseEvent(self, event):
        self.is_follow_mouse = False
        self.setCursor(QCursor(Qt.ArrowCursor))

    def quit(self):
        self.close()
        sys.exit()

    def hide(self):
        self.lb_nono.setVisible(False)

    def display(self):
        self.lb_nono.setVisible(True)
