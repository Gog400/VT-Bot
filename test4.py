import win32gui, win32api, win32con, ctypes, win32ui
import re

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



# steam = FindWindow_bySearch('Steam')
# paint = FindWindow_bySearch('test.jpg - Paint')

# ppos = getCentre(paint)

# print(ppos)
# win32gui.ShowWindow(paint, win32con.SW_RESTORE)
# win32gui.SetForegroundWindow(paint)
# win32gui.EnableWindow(paint, True)

# print(ppos, ' Done!')
