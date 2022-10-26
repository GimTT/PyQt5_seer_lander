# IMPORT PACKAGES START
from PyQt5.QtCore import QEventLoop, QTimer
import win32api
import win32process


# IMPORT PACKAGES END

def __init__():
    # 大漠插件
    global dm
    # 绑定大漠状态
    global bind_status
    # 当前路径
    global current_path
    # pid
    global pid


def dm_drive_delay(time=100):
    loop = QEventLoop()
    QTimer.singleShot(time, loop.quit)
    loop.exec()


def dm_drive_xy_memory(dm_pid):
    hProcess = win32api.OpenProcess(2035711, False, dm_pid)
    pmc = win32process.GetProcessMemoryInfo(hProcess)
    if pmc != {}:
        win32api.CloseHandle(hProcess)
        a = 1024 * 1024
        return pmc['WorkingSetSize'] // a
    win32api.CloseHandle(hProcess)
    return 0


def dm_drive_find_pic(x1, y1, x2, y2, bmp, color, sin, code, pos):
    flag, pos['x'], pos['y'] = dm.FindPic(x1, y1, x2, y2, bmp, color, sin, code)
    return flag


def dm_drive_loop_find_click(x1, y1, x2, y2, bmp, color, sin, code, pos, time):
    for i in range(time):
        dm_drive_delay(50)
        flag, pos['x'], pos['y'] = dm.FindPic(x1, y1, x2, y2, bmp, color, sin, code)
        if pos['x'] > 0 and pos['y'] > 0:
            # print('识别到' + bmp)
            # print('点击' + bmp, pos['x'], pos['y'])
            dm.MoveTo(pos['x'], pos['y'])
            dm.LeftClick()
            return flag

    return -1
