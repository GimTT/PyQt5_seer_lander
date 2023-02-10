import math
import win32api
import win32con
import win32gui
import win32print


class DisplayBase:

    def __init__(self):
        self.hdc = win32gui.GetDC(0)
        self.width = None
        self.height = None
        self.current_width = None
        self.current_height = None
        self.scale = None
        self.get_screen_scale_rate()

    def get_screen_resolution(self):
        sx = win32print.GetDeviceCaps(self.hdc, win32con.DESKTOPHORZRES)
        sy = win32print.GetDeviceCaps(self.hdc, win32con.DESKTOPVERTRES)
        return sx, sy

    @staticmethod
    def get_screen_current():
        sx = win32api.GetSystemMetrics(win32con.SM_CXSCREEN)
        sy = win32api.GetSystemMetrics(win32con.SM_CYSCREEN)
        return sx, sy

    def get_screen_scale_rate(self):
        screen_x, screen_y = self.get_screen_resolution()
        current_x, current_y = self.get_screen_current()
        self.width = screen_x
        self.height = screen_y
        self.current_width = current_x
        self.current_height = current_y
        rate = math.ceil((screen_x * 100) / current_x)
        self.scale = rate
        return rate
