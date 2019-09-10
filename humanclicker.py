from humancurve import HumanCurve
import win32gui, win32api, win32con, ctypes
from time import sleep
from random import uniform, randint


class HumanClicker():

    def move(self, toPoint, duration=2, humanCurve=None):

        fromPoint = win32api.GetCursorPos()

        if not humanCurve:
            humanCurve = HumanCurve(fromPoint, toPoint)

        for point in humanCurve.points:
            sleep(duration / len(humanCurve.points))
            ctypes.windll.user32.SetCursorPos(int(point[0]), int(point[1]))

        hc.rightClick()

    # def leftClick():
    #     ctypes.windll.user32.mouse_event(2, 0, 0, 0,0) # left down
    #     sleep(uniform(0.05, 0.15))
    #     ctypes.windll.user32.mouse_event(4, 0, 0, 0,0) # left up
    #
    # def rightClick():
    #     ctypes.windll.user32.mouse_event(8, 0, 0, 0,0) # Right down
    #     sleep(uniform(0.05, 0.15))
    #     ctypes.windll.user32.mouse_event(10, 0, 0, 0,0) # Right up

    def leftClick():
        pos = win32api.GetCursorPos()
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, pos[0], pos[1], 0, 0)
        sleep(uniform(0.05, 0.15))
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, pos[0], pos[1], 0, 0)

    def rightClick():
        pos = win32api.GetCursorPos()
        win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTDOWN, pos[0], pos[1], 0, 0)
        sleep(uniform(0.05, 0.15))
        win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTUP, pos[0], pos[1], 0, 0)

    def real_click(LorR):
        '''This function clicks the mouse with realistic errors:
            occasional accidental right click
            occasional double click
            occasional no click
        '''
        if randint(1, 19) != 1:
            sleep(93 / randint(83,201))
            if LorR == 'Left':
                HumanClicker.leftClick()
            else:
                HumanClicker.rightClick()
        else:
            tmp_rand = randint(1, 3)
            if tmp_rand == 1:
                #double click
                if LorR == 'Left':
                    HumanClicker.leftClick()
                    sleep(randint(43, 113) / 1000)
                    HumanClicker.leftClick()
                else:
                    HumanClicker.rightClick()
                    sleep(randint(43, 113) / 1000)
                    HumanClicker.rightClick()

            elif tmp_rand == 2:
                if LorR == 'Left':
                    HumanClicker.leftClick()
                    sleep(randint(43, 113) / 1000)
                    HumanClicker.rightClick()
