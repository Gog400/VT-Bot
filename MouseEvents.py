import win32gui, win32api, win32con, ctypes
from time import sleep

class Mouse:
    """It simulates the mouse"""
    MOUSEEVENTF_MOVE = 0x0001 # mouse move
    MOUSEEVENTF_LEFTDOWN = 0x0002 # left button down
    MOUSEEVENTF_LEFTUP = 0x0004 # left button up
    MOUSEEVENTF_RIGHTDOWN = 0x0008 # right button down
    MOUSEEVENTF_RIGHTUP = 0x0010 # right button up
    MOUSEEVENTF_MIDDLEDOWN = 0x0020 # middle button down
    MOUSEEVENTF_MIDDLEUP = 0x0040 # middle button up
    MOUSEEVENTF_WHEEL = 0x0800 # wheel button rolled
    MOUSEEVENTF_ABSOLUTE = 0x8000 # absolute move
    SM_CXSCREEN = 0
    SM_CYSCREEN = 1

    def get_position():
        """get mouse position"""
        return win32api.GetCursorPos()

    def _do_event(flags, x_pos, y_pos, data, extra_info):
        """generate a mouse event"""
        x_calc = 65536 * x_pos // 1920 + 1
        y_calc = 65536 * y_pos // 1080 + 1
        return win32api.mouse_event(flags, x_calc, y_calc, data, extra_info)

    def _get_button_value(button_name, button_up=False):
        """convert the name of the button into the corresponding value"""
        buttons = 0
        if button_name.find("right") >= 0:
            buttons = Mouse.MOUSEEVENTF_RIGHTDOWN
        if button_name.find("left") >= 0:
            buttons = buttons + Mouse.MOUSEEVENTF_LEFTDOWN
        if button_name.find("middle") >= 0:
            buttons = buttons + Mouse.MOUSEEVENTF_MIDDLEDOWN
        if button_up:
            buttons = buttons << 1
        return buttons

    def move_mouse(pos):
        print(pos)
        """move the mouse to the specified coordinates"""
        (x, y) = pos
        old_pos = Mouse.get_position()
        x =  x if (x != -1) else old_pos[0]
        y =  y if (y != -1) else old_pos[1]
        Mouse._do_event(win32con.MOUSEEVENTF_MOVE + win32con.MOUSEEVENTF_ABSOLUTE, x, y, 0, 0)

    def press_button(pos=(-1, -1), button_name="left", button_up=False):
        """push a button of the mouse"""
        Mouse.move_mouse(pos)
        Mouse._do_event(Mouse._get_button_value(button_name, button_up), 0, 0, 0, 0)

    def click(pos=(-1, -1), button_name= "left"):
        """Click at the specified placed"""
        Mouse.move_mouse(pos)
        Mouse._do_event(Mouse._get_button_value(button_name, False)+Mouse._get_button_value(button_name, True), 0, 0, 0, 0)

    def double_click (pos=(-1, -1), button_name="left"):
        """Double click at the specifed placed"""
        for i in xrange(2):
            Mouse.click(pos, button_name)
sleep(1)
Mouse.click(button_name="Right")
