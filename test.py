# def writeText(text):
#     # if __name__ == '__main__':
#     queue.append(text)
#     for c in queue:
#         time.sleep(0.5)
#         PressKey(c)
#         time.sleep(0.5)
#         ReleaseKey(c)
#
# writeText("Titan's treasure")
# from MouseEvents import Mouse
# import time
#
# mouse = Mouse()
# mouse.click((20, 10), "left")
# time.sleep(2.0)
#
# mouse.click((100, 100), "right")

# import ctypes
# MOUSEEVENTF_MOVE = 0x0001 # mouse move
# MOUSEEVENTF_ABSOLUTE = 0x8000 # absolute move
# MOUSEEVENTF_MOVEABS = MOUSEEVENTF_MOVE + MOUSEEVENTF_ABSOLUTE
#
# MOUSEEVENTF_LEFTDOWN = 0x0002 # left button down
# MOUSEEVENTF_LEFTUP = 0x0004 # left button up
# MOUSEEVENTF_CLICK = MOUSEEVENTF_LEFTDOWN + MOUSEEVENTF_LEFTUP
#
# def click(x, y):
#     #move first
#     x = 65536L * x / ctypes.windll.user32.GetSystemMetrics(0) + 1
#     y = 65536L * y / ctypes.windll.user32.GetSystemMetrics(1) + 1
#     ctypes.windll.user32.mouse_event(MOUSEEVENTF_MOVEABS, x, y, 0, 0)
#
#     #then click
#     ctypes.windll.user32.mouse_event(MOUSEEVENTF_CLICK, 0, 0, 0, 0)


t = 100
while t > 0:
    t = t//2
    print(t)
