import win32gui, win32api, win32con, ctypes, win32ui
from pyclick.humanclicker import HumanClicker

hc = HumanClicker()
# def mnc():
#     hc.move((600,300), 1)
#     hc.real_click('Left')


# desktop = win32gui.GetDesktopWindow()
#
# l,t,r,b = win32gui.GetWindowRect(self.hwnd)

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

find('Steam', 960, 540, 200, 200)


#
# dt_l, dt_t, dt_r, dt_b = win32gui.GetWindowRect(desktop)
# centre_x, centre_y = win32gui.ClientToScreen( desktop, ( (dt_r-dt_l)//2, (dt_b-dt_t)//2) )
