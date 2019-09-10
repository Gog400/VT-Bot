import win32gui, win32api, win32con, ctypes, win32ui
from pyclick.humanclicker import HumanClicker
import re
import time
from MouseEvents import Mouse

hc = HumanClicker()
# def mnc():
#     hc.move((600,300), 1)
#     hc.real_click('Left')


# desktop = win32gui.GetDesktopWindow()
#
# l,t,r,b = win32gui.GetWindowRect(self.hwnd)

def FindWindow_bySearch(pattern):
    window_list = []
    win32gui.EnumWindows(lambda hWnd, param: param.append(hWnd), window_list)
    for each in window_list:
        if re.search(pattern, win32gui.GetWindowText(each)) is not None: # win32gui.GetWindowText(each) - name (for ex: Steam)
            return each # Window ID (for ex: 66950)

def getWindow_W_H(hwnd):
    # 取得目標視窗的大小
    left, top, right, bot = win32gui.GetWindowRect(hwnd)
    width = right - left - 15
    height = bot - top - 11
    print(left, top, width, height)
    return (left, top, width, height)

def getCentre(hwnd):
    _left, _top, _right, _bottom = win32gui.GetWindowRect(hwnd)
    centreX = (_right - _left)//2 + _left
    centreY = (_bottom - _top)//2 + _top
    return (centreX, centreY)

def doEvent(button, pos):
    # lParam = win32api.MAKELONG(pos[0], pos[1])
    (x_pos, y_pos) = pos
    x_calc = 65536 * x_pos // 1920 + 1
    y_calc = 65536 * y_pos // 1080 + 1
    win32api.mouse_event(button, x_calc, y_calc, 0, 0) # win32con.MOUSEEVENTF_LEFTDOWN
    time.sleep(0.1)

    # win32api.SendMessage(hwnd, button, 0, lParam) # win32con.WM_MOUSEMOVE | win32con.WM_LBUTTONDOWN | win32con.WM_RBUTTONUP
    # time.sleep(0.1)

# def coordsTransition(clientHwnd, transHwnd):
#     _left, _top, _right, _bottom = win32gui.GetWindowRect(clientHwnd)
#
#     left, top, right, bottom = win32gui.GetWindowRect(transHwnd)
#     # left, top = win32gui.ClientToScreen(transHwnd, (_left, _top))
#     # right, bottom = win32gui.ClientToScreen(transHwnd, (_right, _bottom))
#
#     clientW = _right - _left
#     clientH = _bottom - _top
#     clientCentreX = clientW/2 + _right
#     clientCentreY = clientH/2 + _bottom
#     transW = right - left
#     transH = bottom - top
#     print('Transtition from: ', _left, _top, _right, _bottom, 'W: ', clientW, 'H: ', clientH)
#     print('Transtition to: ', left, top, right, bottom, 'W: ', transW, 'H: ', transH)
#     return (left, top, right, bottom)

def find(hWnd, x, y, w, h):

    hWnd = win32gui.FindWindow(None, hWnd)

    # desktop = win32gui.GetDesktopWindow()
    # print('desktop: ', desktop)
    # pycwnd = win32ui.CreateWindowFromHandle(hWnd)

    # _left, _top, _right, _bottom = win32gui.GetClientRect(hWnd)
    # #
    # left, top = win32gui.ClientToScreen(hWnd, (_left, _top))
    # right, bottom = win32gui.ClientToScreen(hWnd, (_right, _bottom))


    win32gui.ShowWindow(hWnd, win32con.SW_RESTORE) # разворачивает окно
    # win32gui.SetActiveWindow(hWnd)
    # win32gui.SetFocus(hWnd) # отказывает в доступе
    # win32gui.SetForegroundWindow(hWnd)
    # win32gui.BringWindowToTop(paint)

    bbox = win32gui.GetWindowRect(hWnd)

    win32gui.MoveWindow(hWnd, x, y, w, h, True) # последний параметр(Тру) - это вроде активировать ли окно
    print(bbox)

    lParam = win32api.MAKELONG(x, y) # как я понял Эль парам - это координаты Икс и Игрик, представленной одной переменной.
    # print(lParam)


    # win32api.SendMessage(hWnd, win32con.WM_MOUSEMOVE, 0, lParam)
    # win32api.SendMessage(hWnd, win32con.WM_LBUTTONDOWN, 0, lParam) # wParam = win32con.MK_LBUTTON
    # win32api.SendMessage(hWnd, win32con.WM_LBUTTONUP, 0, lParam)

    print('SUUUCK')

    # hc.move((600,300), 1)

# find('Steam', 960, 540, 200, 200)
steam = FindWindow_bySearch('Steam')
paint = FindWindow_bySearch('test.jpg - Paint')

win32gui.ShowWindow(paint, win32con.SW_RESTORE)
win32gui.SetForegroundWindow(paint)
win32gui.EnableWindow(paint, True)

# win32api.mouse_event(win32con.MOUSEEVENTF_MOVE, 400, 400, 0, 0) # win32con.MOUSEEVENTF_LEFTDOWN

# win32gui.MoveWindow(paint, 100, 100, 400, 400, 1)
ppos = getCentre(paint)
print(ppos)
time.sleep(1)
Mouse.move_mouse(ppos)
doEvent(win32con.MOUSEEVENTF_LEFTDOWN, ppos)
doEvent(win32con.MOUSEEVENTF_LEFTUP, ppos)

# doEvent(paint, win32con.WM_MOUSEMOVE, getCentre(paint))
# doEvent(paint, win32con.WM_LBUTTONDOWN, getCentre(paint))
# doEvent(paint, win32con.WM_LBUTTONUP, getCentre(paint))
print('Done!')
# win32ui.MessageBox(str(getCentre(steam)), 'Position finder', 0) # create a dialog window (message, title, windowType)
