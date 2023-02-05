# IMPORT PACKAGES START
import os
import sys

import win32gui
from PyQt5 import QtCore
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox, QDesktopWidget
from pycaw.pycaw import AudioUtilities
# IMPORT PACKAGES END

# IMPORT USER PY FILE START
import seer_lander_register
import seer_lander_nono
import seer_lander_speed
import seer_lander_auto
import seer_lander_ui_main
import seer_lander_dm_drive
import seer_lander_knapsack
import game_window_thread

# IMPORT USER PY FILE END


DEBUG_MODE = False  # 调试模式

# 相关参数
MAIN_WINDOW_WIDTH = 960
MAIN_WINDOW_HEIGHT = 560
AXWIDGET_WINDOW_WIDTH = 980
AXWIDGET_WINDOW_HEIGHT = 580


# 主窗口类
class MainLanderUi(QMainWindow, seer_lander_ui_main.Ui_MainWindow):

    # 初始化部分
    def __init__(self):
        super().__init__()

        # Threads handle def begin
        self.seer_game_window_thread_handle = None
        # Threads handle def end

        # 设置图标
        self.setWindowIcon(QIcon('ini/GimTT_Lander_img.ico'))

        # 自动确认的列表
        self.auto_click_end_list = []

        # dm驱动
        seer_lander_dm_drive.bind_status = False
        seer_lander_dm_drive.current_path = os.getcwd()
        self.pid = None

        # nono窗口
        self.nono = None
        self.nono_init()

        # speed窗口
        self.speed_window_t = seer_lander_speed.SpeedUi()

        # 脚本窗口
        self.auto_window_t = seer_lander_auto.AutoUi()
        self.auto_window_t.signal_auto_2_lander.connect(self.get_signal)  # 链接信号

        # 换背包窗口
        self.pack_window_t = seer_lander_knapsack.SeerFreeKnapsackUi()
        self.pack_window_t.signal_pack_2_lander.connect(self.get_signal)  # 连接信号

        # 登陆器窗口
        self.setupUi(self)
        # self.setFixedSize(self.width(), self.height())
        # self.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint)  # 置顶lander
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)  # 不显示边框
        # self.setWindowFlags(QtCore.Qt.CustomizeWindowHint)  # 有透明边框
        self.start_seer_game_window_thread()
        self.lock_music()

    # 函数功能：多线程方式启动赛尔号窗口（缓解卡顿）
    def start_seer_game_window_thread(self):
        self.seer_game_window_thread_handle = game_window_thread.GameWindowThread(self.axWidget)
        self.seer_game_window_thread_handle.start()

    # 函数功能：启动nono
    def nono_init(self):
        self.nono = seer_lander_nono.TablePet()  # 声明
        self.nono.lb_nono.signal_nono_2_lander.connect(self.get_signal)  # 链接信号
        self.nono.show()  # 显示

    # 函数功能：移动到屏幕中心
    def move_2_center(self):
        center_pointer = QDesktopWidget().availableGeometry().center()
        x = center_pointer.x()
        y = center_pointer.y()
        tl_x, tl_y, width, height = self.frameGeometry().getRect()  # 窗口左上角坐标(x,y)、宽高(W, H)
        self.move(x - width / 2, y - height / 2)

    # 函数功能：缩放   BEGIN
    def size_max(self):
        desktop = QApplication.desktop()
        base = (desktop.width() / MAIN_WINDOW_WIDTH) * 0.9
        self.resize(MAIN_WINDOW_WIDTH * base, MAIN_WINDOW_HEIGHT * base)
        self.groupBox.resize(MAIN_WINDOW_WIDTH * base, MAIN_WINDOW_HEIGHT * base)
        self.axWidget.resize(AXWIDGET_WINDOW_WIDTH * base + 50, AXWIDGET_WINDOW_HEIGHT * base + 50)
        self.move_2_center()

    def size_50percent(self):
        self.resize(480, 280)
        self.groupBox.resize(480, 280)
        self.axWidget.resize(500, 300)
        self.move_2_center()

    def size_75percent(self):
        self.resize(720, 420)
        self.groupBox.resize(720, 420)
        self.axWidget.resize(740, 440)
        self.move_2_center()

    def size_125percent(self):
        self.resize(1200, 700)
        self.groupBox.resize(1200, 700)
        self.axWidget.resize(1225, 725)
        self.move_2_center()

    def size_150percent(self):
        self.resize(1440, 840)
        self.groupBox.resize(1440, 840)
        self.axWidget.resize(1470, 870)
        self.move_2_center()

    def size_reset(self):
        self.resize(960, 560)
        self.groupBox.resize(960, 560)
        self.axWidget.resize(980, 580)
        self.move_2_center()

    # 函数功能：缩放   ENG

    # 函数功能：绑定大漠
    def lander_ie_bind_dm(self):
        # 获取游戏句柄
        main_window_pid = self.winId().__int__()

        child_window_pid = win32gui.GetWindow(main_window_pid, 5)
        child_window_pid = win32gui.GetWindow(child_window_pid, 5)
        child_window_pid = win32gui.GetWindow(child_window_pid, 5)
        child_window_pid = win32gui.GetWindow(child_window_pid, 5)
        child_window_pid = win32gui.GetWindow(child_window_pid, 5)
        child_window_pid = win32gui.GetWindow(child_window_pid, 5)
        child_window_pid = win32gui.GetWindow(child_window_pid, 5)
        self.pid = child_window_pid
        seer_lander_dm_drive.pid = child_window_pid
        # 初始化大漠
        seer_lander_register.dm_register()

        # 绑定窗口
        if seer_lander_dm_drive.dm.BindWindow(self.pid, "dx2", "windows", "windows", 1) == 0:
            pass
        else:
            seer_lander_dm_drive.bind_status = True

        # 设置识图目录
        path = os.getcwd() + '/autoImg'
        seer_lander_dm_drive.dm.SetPath(path)
        seer_lander_dm_drive.dm.SetDict(0, os.getcwd() + "/ini" + "/ziku.txt")

        # 自动登录
        pos = {}
        seer_lander_dm_drive.dm_drive_find_pic(0, 0, 1000, 600, "login.bmp", "000000", 0.8, 0, pos)  # 查找登录按钮
        if pos['x'] != -1 and pos['y'] != -1:
            seer_lander_dm_drive.dm_drive_delay(10)
            seer_lander_dm_drive.dm.MoveTo(pos['x'] - 379, pos['y'] - 65)
            seer_lander_dm_drive.dm.LeftClick()

    # 注册自动确认函数（会执行）
    def auto_click_end_register(self):
        # 自动确认
        if self.load_auto_click_end_list() != 0:
            # 没有执行自动确认
            # print('找不到auto_click_end_init.txt')
            msg_box = QMessageBox(QMessageBox.Warning, "文件出错", "自动确认功能未启动")
            msg_box.exec_()
            return

        else:
            self.auto_click_end_begin()

    # 函数功能：将自动确认图片列表读入（0：成功/-1：失败）
    def load_auto_click_end_list(self):
        # 读入自动确认的列表 （自动确认部分应放在dm绑定成功之后）
        try:
            auto_click_end_list_file = open(os.getcwd() + '/autoImg' + "/自动确认" + "/auto_click_end.txt", "rb")
            for file_name_index in auto_click_end_list_file:
                self.auto_click_end_list.append(file_name_index.decode("gb2312").replace("\n", "").replace("\r", ""))
            auto_click_end_list_file.close()

        except:
            # print('找不到auto_click_end_init.txt')
            msg_box = QMessageBox(QMessageBox.Warning, "文件出错", "找不到auto_click_end_init.txt")
            msg_box.exec_()
            return -1

        return 0

    # 函数功能：按列表自动确认（该函数以阻塞方式运行）（运行时间：50 * 图片数量）（0：成功/-1：失败）
    def auto_click_end_begin(self):
        while 1:
            seer_lander_dm_drive.dm_drive_delay(100)
            for image_index in self.auto_click_end_list:
                pos = {}
                seer_lander_dm_drive.dm_drive_find_pic(0, 0, 1000, 600,
                                                       os.getcwd() + '/' + 'autoImg' + '/' + "自动确认" + '/' + image_index,
                                                       "000000", 0.8, 0, pos)
                if pos['x'] != -1 and pos['y'] != -1:
                    seer_lander_dm_drive.dm.MoveTo(pos['x'], pos['y'])
                    seer_lander_dm_drive.dm.LeftClick()
                    continue  # 判断到了就不判断了（有时更快）

    # 函数功能：进入仓库
    @staticmethod
    def go_to_genie_library():
        pos = {}
        seer_lander_dm_drive.dm_drive_find_pic(0, 0, 1000, 600,
                                               os.getcwd() + '/' + 'autoImg' + '/' + "换背包" + '/' + "genie_button.bmp",
                                               "000000", 0.8, 0, pos)
        if pos['x'] != -1 and pos['y'] != -1:
            seer_lander_dm_drive.dm_drive_delay(10)
            seer_lander_dm_drive.dm.MoveTo(pos['x'], pos['y'])
            seer_lander_dm_drive.dm.LeftClick()

        # 等待背包被打开
        seer_lander_dm_drive.dm_drive_delay(1000)

        seer_lander_dm_drive.dm_drive_find_pic(0, 0, 1000, 600,
                                               os.getcwd() + '/' + 'autoImg' + '/' + "换背包" + '/' + "to_library.bmp",
                                               "000000", 0.8, 0, pos)  # 查找入库按钮
        if pos['x'] != -1 and pos['y'] != -1:
            seer_lander_dm_drive.dm_drive_delay(10)
            seer_lander_dm_drive.dm.MoveTo(pos['x'] + 407, pos['y'] - 89)
            for i in range(12):
                seer_lander_dm_drive.dm.LeftClick()
                seer_lander_dm_drive.dm_drive_delay(200)

        # 至此说明找不到入库按钮
        else:
            # print('未识别到')
            return -1

        seer_lander_dm_drive.dm_drive_loop_find_click(0, 0, 1000, 600,
                                                      os.getcwd() + '/' + 'autoImg' + '/' + "换背包" + '/' + "go_to_library.bmp",
                                                      "000000",
                                                      0.8, 0, pos, 40)  # 2s
        # 等待转到仓库
        seer_lander_dm_drive.dm_drive_delay(500)

        seer_lander_dm_drive.dm_drive_find_pic(0, 0, 1000, 600,
                                               os.getcwd() + '/' + 'autoImg' + '/' + "换背包" + '/' + "search_genie.bmp",
                                               "000000", 0.8, 0, pos)
        if pos['x'] != -1 and pos['y'] != -1:
            seer_lander_dm_drive.dm_drive_delay(10)
            seer_lander_dm_drive.dm.MoveTo(pos['x'], pos['y'])
            seer_lander_dm_drive.dm.LeftClick()

    # 函数功能：放一只精灵到背包
    @staticmethod
    def search_genie():
        seer_lander_dm_drive.dm_drive_delay(100)

        seer_lander_dm_drive.dm.KeyDownChar("enter")
        seer_lander_dm_drive.dm_drive_delay(10)
        seer_lander_dm_drive.dm.KeyUpChar("enter")

        seer_lander_dm_drive.dm_drive_delay(100)

        pos = {}
        seer_lander_dm_drive.dm_drive_find_pic(0, 0, 1000, 600,
                                               os.getcwd() + '/' + 'autoImg' + '/' + "换背包" + '/' + "to_pack.bmp",
                                               "000000", 0.8, 0, pos)
        if pos['x'] != -1 and pos['y'] != -1:
            seer_lander_dm_drive.dm_drive_delay(100)
            seer_lander_dm_drive.dm.MoveTo(pos['x'], pos['y'])
            seer_lander_dm_drive.dm.LeftClick()

        seer_lander_dm_drive.dm_drive_delay(100)

        seer_lander_dm_drive.dm_drive_find_pic(0, 0, 1000, 600,
                                               os.getcwd() + '/' + 'autoImg' + '/' + "换背包" + '/' + "end.bmp",
                                               "000000", 0.8, 0, pos)
        if pos['x'] != -1 and pos['y'] != -1:
            seer_lander_dm_drive.dm_drive_delay(10)
            seer_lander_dm_drive.dm.MoveTo(pos['x'], pos['y'])
            seer_lander_dm_drive.dm.LeftClick()

        seer_lander_dm_drive.dm_drive_delay(500)

        seer_lander_dm_drive.dm_drive_find_pic(0, 0, 1000, 600,
                                               os.getcwd() + '/' + 'autoImg' + '/' + "换背包" + '/' + "close.bmp",
                                               "000000", 0.8, 0, pos)
        if pos['x'] != -1 and pos['y'] != -1:
            seer_lander_dm_drive.dm_drive_delay(10)
            seer_lander_dm_drive.dm.MoveTo(pos['x'], pos['y'])
            seer_lander_dm_drive.dm.LeftClick()

        seer_lander_dm_drive.dm_drive_delay(500)

        seer_lander_dm_drive.dm_drive_find_pic(0, 0, 1000, 600,
                                               os.getcwd() + '/' + 'autoImg' + '/' + "换背包" + '/' + "search_genie_pic.bmp",
                                               "000000", 0.8, 0, pos)
        if pos['x'] != -1 and pos['y'] != -1:
            seer_lander_dm_drive.dm_drive_delay(10)
            seer_lander_dm_drive.dm.MoveTo(pos['x'] - 20, pos['y'])
            seer_lander_dm_drive.dm.LeftClick()

        for i in range(10):
            seer_lander_dm_drive.dm.KeyDownChar("back")
            seer_lander_dm_drive.dm_drive_delay(10)
            seer_lander_dm_drive.dm.KeyUpChar("back")

    # 函数功能：返回背包界面
    @staticmethod
    def return_pack():
        seer_lander_dm_drive.dm_drive_delay(500)

        pos = {}
        seer_lander_dm_drive.dm_drive_find_pic(0, 0, 1000, 600,
                                               os.getcwd() + '/' + 'autoImg' + '/' + "换背包" + '/' + "go_to_pack.bmp",
                                               "000000", 0.8, 0, pos)
        if pos['x'] != -1 and pos['y'] != -1:
            seer_lander_dm_drive.dm_drive_delay(10)
            seer_lander_dm_drive.dm.MoveTo(pos['x'], pos['y'])
            seer_lander_dm_drive.dm.LeftClick()

    # 函数功能：取消静音
    @staticmethod
    def lock_music():
        sessions = AudioUtilities.GetAllSessions()
        for session in sessions:
            volume = session.SimpleAudioVolume

            # 只有在打包后生效，调试时进程是python虚拟机
            if DEBUG_MODE:
                if session.Process and session.Process.name() == "python.exe":
                    volume.SetMute(1, None)
            else:
                if session.Process and session.Process.name() == "seer_lander_main.exe":
                    volume.SetMute(1, None)

    # 函数功能：静音
    @staticmethod
    def unlock_music():
        sessions = AudioUtilities.GetAllSessions()
        for session in sessions:
            volume = session.SimpleAudioVolume

            # 只有在打包后生效，调试时进程是python虚拟机
            if DEBUG_MODE:
                if session.Process and session.Process.name() == "python.exe":
                    volume.SetMute(0, None)
            else:
                if session.Process and session.Process.name() == "seer_lander_main.exe":
                    volume.SetMute(0, None)

    # 函数功能：换背包
    def seer_pack_change(self):
        if self.go_to_genie_library() == -1:
            msg_box = QMessageBox(QMessageBox.Warning, "脚本出错", "未识别仓库图标，脚本停止")
            msg_box.exec_()
            return
        for i in range(12):
            if self.pack_window_t.packGenie_view_list[i].text() != '':
                seer_lander_dm_drive.dm.SendString(self.pid, self.pack_window_t.packGenie_view_list[i].text())
                self.search_genie()
        self.return_pack()

    # 函数功能：多线程脚本线程服务函数
    def auto_84_task(self):
        pass

    # 函数功能：根据信号执行函数
    def get_signal(self, connect):
        # python3.10+新增了switch语句，但本项目的环境为3.6.8
        if connect == 0:  # 刷新
            self.seer_game_window_thread_handle.refresh()

        elif connect == 1:  # 变速窗口
            self.speed_window_t.show()
            self.speed_window_t.speed_view_move()

        elif connect == 2:  # 静音
            self.lock_music()

        elif connect == 3:  # 打开声音
            self.unlock_music()

        elif connect == 6:  # 打开换背包窗口
            self.pack_window_t.show()
            self.pack_window_t.pack_view_move()

        elif connect == 7:  # 换一号背包
            self.seer_pack_change()

        elif connect == 92:
            self.seer_game_window_thread_handle.size_50percent()
            self.size_50percent()

        elif connect == 93:
            self.seer_game_window_thread_handle.size_75percent()
            self.size_75percent()

        elif connect == 94:
            self.seer_game_window_thread_handle.size_max()
            self.size_max()

        elif connect == 95:
            self.seer_game_window_thread_handle.size_150percent()
            self.size_150percent()

        elif connect == 96:
            self.seer_game_window_thread_handle.size_125percent()
            self.size_125percent()

        elif connect == 97:
            self.seer_game_window_thread_handle.size_reset()
            self.size_reset()

        elif connect == 98:  # 自动84
            pass

        elif connect == 99:  # nono换皮肤
            self.nono.close()  # 先关掉对象
            self.nono_init()  # 重新打开


if __name__ == '__main__':
    landerApp = QApplication(sys.argv)
    MainWindow = MainLanderUi()
    MainWindow.show()
    seer_lander_dm_drive.dm_drive_delay(3000)
    MainWindow.lander_ie_bind_dm()
    MainWindow.auto_click_end_register()

    landerApp.exit(landerApp.exec_())
