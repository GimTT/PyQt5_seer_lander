# IMPORT PACKAGES START
import math
import os
import sys

import win32gui
from PyQt5 import QtCore
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox, QDesktopWidget
from pycaw.pycaw import AudioUtilities
# IMPORT PACKAGES END

# IMPORT USER PY FILE START
from global_define import *
import seer_lander_register
import seer_lander_nono
import seer_lander_speed
import seer_lander_auto
import seer_lander_ui_main
import seer_lander_dm_drive
import seer_lander_knapsack
import game_window_thread
import display_base

# IMPORT USER PY FILE END

'''
system_window(1920 * 1080)  16 : 9
lander_window(960 * 560)    
WIDTH       |       2 : 1
HEIGHT      |       27 : 14
'''


# 主窗口类
class MainLanderUi(QMainWindow, seer_lander_ui_main.Ui_MainWindow):

    # 初始化部分
    def __init__(self):
        super().__init__()
        # Threads handle def begin
        self.seer_game_window_thread_handle = None
        # Threads handle def end

        # Create Object being

        # Create Object end

        self.desktop = QApplication.desktop()
        self.desktopWidth = int(self.desktop.width())
        self.desktopHeight = int(self.desktop.height())
        self.width = MAIN_WINDOW_WIDTH
        self.height = MAIN_WINDOW_HEIGHT
        self.scale = None

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
        self.init_size()
        self.set_size(self.width, self.height)

        self.disable_title_bar()
        self.start_seer_game_window_thread()
        self.lock_music()

    # name      :   set_size
    # parameter :   width:宽度, height: 宽度
    # function  :   设置窗口大小
    def set_size(self, width, height):
        self.resize(width, height)
        self.groupBox.resize(width, height)
        self.axWidget.resize(width + 100, height + 100)
        self.move_to_center()

    # name      :   calculate_screen_scale
    # parameter :   none
    # function  :   计算屏幕比例
    def init_size(self):
        if self.desktop.width() > self.desktopHeight:  # 若屏幕宽大于高
            self.height = int(self.desktopHeight * MAIN_WINDOW_HEIGHT / DISPLAY_HEIGHT_1080P)
            self.width = int(self.height * MAIN_WINDOW_WIDTH / MAIN_WINDOW_HEIGHT)

    # name      :   calculate_screen_scale
    # parameter :   scale:缩放比例(小数)
    # function  :   计算屏幕比例
    def reset_size(self, scale):
        self.set_size(int(self.width * scale), int(self.height * scale))
        game_area_scale = math.ceil(game_scale * scale)
        if game_area_scale % 2 != 0 and game_area_scale % 10 != 5:
            game_area_scale += 1
        if DEBUG_MODE:
            print("[scale:%d]" % game_area_scale)
        self.seer_game_window_thread_handle.set_size(game_area_scale)
        self.move_to_center()

    # name      :   show_title_bar
    # parameter :   none
    # function  :   显示标题栏
    def enable_title_bar(self):
        self.setWindowFlags(QtCore.Qt.Widget)  # 重设标签（去除所有flag）
        self.setWindowFlags(QtCore.Qt.WindowMinimizeButtonHint)  # 禁用最小化和关闭按钮
        # self.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint)  # 置顶窗口
        #
        # self.setWindowFlags(QtCore.Qt.FramelessWindowHint)  # 不显示边框
        # self.setWindowFlags(QtCore.Qt.CustomizeWindowHint)  # 有透明边框

    # name      :   disable_title_bar
    # parameter :   none
    # function  :   不显示标题栏
    def disable_title_bar(self):
        self.setWindowFlags(QtCore.Qt.Widget)  # 重设标签（去除所有flag）
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)  # 不显示边框

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
    def move_to_center(self):
        center_pointer = QDesktopWidget().availableGeometry().center()
        x = center_pointer.x()
        y = center_pointer.y()
        tl_x, tl_y, width, height = self.frameGeometry().getRect()  # 窗口左上角坐标(x,y)、宽高(W, H)
        self.move(x - width / 2, y - height / 2)

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

        if game_scale != 0:
            self.seer_game_window_thread_handle.set_size(game_scale)

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
            self.reset_size(0.5)

        elif connect == 93:
            self.reset_size(0.75)

        elif connect == 94:
            self.reset_size(1.75)

        elif connect == 95:
            self.reset_size(1.5)

        elif connect == 96:
            self.reset_size(1.25)

        elif connect == 97:
            self.set_size(self.width, self.height)
            self.seer_game_window_thread_handle.set_size(game_scale)

        elif connect == 98:  # 自动84
            pass

        elif connect == 99:  # nono换皮肤
            self.nono.close()  # 先关掉对象
            self.nono_init()  # 重新打开


if __name__ == '__main__':
    QApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling)
    landerApp = QApplication(sys.argv)
    MainWindow = MainLanderUi()
    MainWindow.show()
    seer_lander_dm_drive.dm_drive_delay(3000)
    MainWindow.lander_ie_bind_dm()
    MainWindow.auto_click_end_register()
    landerApp.exit(landerApp.exec_())
