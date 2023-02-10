import display_base
import math

DEBUG_MODE = False  # 调试模式

DISPLAY_WIDTH_1080P = 1920
DISPLAY_HEIGHT_1080P = 1080
MAIN_WINDOW_WIDTH = 960
MAIN_WINDOW_HEIGHT = 560
AX_WIDGET_WINDOW_WIDTH = 980
AX_WIDGET_WINDOW_HEIGHT = 580

display_base_t = display_base.DisplayBase()  # 获取屏幕信息
windows_desktop_width = display_base_t.width
windows_desktop_height = display_base_t.height
windows_desktop_scale = 0
lander_height = 0
lander_width = 0
game_scale = 0

if windows_desktop_width > windows_desktop_height:  # 若屏幕宽大于高
    lander_height = (windows_desktop_height * MAIN_WINDOW_HEIGHT / DISPLAY_HEIGHT_1080P)
    lander_width = round(lander_height * MAIN_WINDOW_WIDTH / MAIN_WINDOW_HEIGHT)
    windows_desktop_scale = display_base_t.scale
    game_scale = math.ceil((windows_desktop_scale * lander_height / MAIN_WINDOW_HEIGHT * 100) / 100)

if DEBUG_MODE:
    print(
        "[display][windows_desktop_width:%d, windows_desktop_height:%d, lander_width:%d, lander_height:%d, "
        "game_scale:%d]" % (windows_desktop_width, windows_desktop_height, lander_width, lander_height, game_scale))
