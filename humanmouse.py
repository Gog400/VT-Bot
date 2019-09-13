from humancurve import HumanCurve
from win32api import GetCursorPos, SetCursorPos, mouse_event
import win32con
from time import sleep
from random import randint

class HumanMouse():

    def move(toPoint, duration=2, humanCurve=None):
        # moving your mouse in the bezier curve path

        fromPoint = GetCursorPos()

        if not humanCurve:
            humanCurve = HumanCurve(fromPoint, toPoint)

        for point in humanCurve.points:
            sleep(duration / len(humanCurve.points))
            SetCursorPos((int(point[0]), int(point[1])))


    def buttonPressedReleased(button):

        pos = GetCursorPos()

        if button == 'Right':
            mouse_event(win32con.MOUSEEVENTF_RIGHTDOWN, pos[0], pos[1], 0, 0)
            sleep(randint(43, 113) / 1000)
            mouse_event(win32con.MOUSEEVENTF_RIGHTUP, pos[0], pos[1], 0, 0)

        elif button == 'Left':
            mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, pos[0], pos[1], 0, 0)
            sleep(randint(43, 113) / 1000)
            mouse_event(win32con.MOUSEEVENTF_LEFTUP, pos[0], pos[1], 0, 0)



    def click(button1, button2):
        # example: HumanMouse.click('Right', 'Left')
        # button1 - generally used mouse button
        # button2 - missclick mouse button

        sleep(93 / randint(83,201))
        fromPoint = GetCursorPos()

        if randint(1, 19) != 1:
            HumanMouse.buttonPressedReleased(button1)

        else:
            temp_rand = randint(0, 1)

            if temp_rand == 0:
                # double click
                HumanMouse.buttonPressedReleased(button1)
                sleep(randint(43, 113) / 1000)
                HumanMouse.buttonPressedReleased(button1)

            elif temp_rand == 1:
                # missclick
                HumanMouse.buttonPressedReleased(button2)
                sleep(randint(43, 113) / 1000)
                HumanMouse.buttonPressedReleased(button1)
