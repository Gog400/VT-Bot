import win32gui, win32api, win32con, ctypes
from time import sleep
from random import uniform

# def get_line(start, end):
#     """Bresenham's Line Algorithm
#     Produces a list of tuples from start and end
#
#     >>> points1 = get_line((0, 0), (3, 4))
#     >>> points2 = get_line((3, 4), (0, 0))
#     >>> assert(set(points1) == set(points2))
#     >>> print points1
#     [(0, 0), (1, 1), (1, 2), (2, 3), (3, 4)]
#     >>> print points2
#     [(3, 4), (2, 3), (1, 2), (1, 1), (0, 0)]
#     """
#     # Setup initial conditions
#     x1, y1 = start
#     x2, y2 = end
#     dx = x2 - x1
#     dy = y2 - y1
#
#     # Determine how steep the line is
#     is_steep = abs(dy) > abs(dx)
#
#     # Rotate line
#     if is_steep:
#         x1, y1 = y1, x1
#         x2, y2 = y2, x2
#
#     # Swap start and end points if necessary and store swap state
#     swapped = False
#     if x1 > x2:
#         x1, x2 = x2, x1
#         y1, y2 = y2, y1
#         swapped = True
#
#     # Recalculate differentials
#     dx = x2 - x1
#     dy = y2 - y1
#
#     # Calculate error
#     error = int(dx / 2.0)
#     ystep = 1 if y1 < y2 else -1
#
#     # Iterate over bounding box generating points between start and end
#     y = y1
#     points = []
#     for x in range(x1, x2 + 1):
#         coord = (y, x) if is_steep else (x, y)
#         points.append(coord)
#         error -= abs(dy)
#         if error < 0:
#             y += ystep
#             error += dx
#
#     # Reverse the list if the coordinates were swapped
#     if swapped:
#         points.reverse()
#     return points


class Event():

    def pos(x, y):
        # see http://msdn.microsoft.com/en-us/library/ms646260(VS.85).aspx for details
        ctypes.windll.user32.SetCursorPos(x, y)
        # start = win32api.GetCursorPos()

    def leftClick():
        ctypes.windll.user32.mouse_event(2, 0, 0, 0,0) # left down
        sleep(uniform(0.05, 0.15))
        ctypes.windll.user32.mouse_event(4, 0, 0, 0,0) # left up

    def rightClick():
        ctypes.windll.user32.mouse_event(8, 0, 0, 0,0) # Right down
        sleep(uniform(0.05, 0.15))
        ctypes.windll.user32.mouse_event(10, 0, 0, 0,0) # Right up


    def real_click(LorR):
        '''This function clicks the mouse with realistic errors:
            occasional accidental right click
            occasional double click
            occasional no click
        '''
        if randint(1, 19) != 1:
            sleep(93 / randint(83,201))
            if LorR == 'Left':
                leftClick()
            else:
                rightClick()
        else:
            tmp_rand = randint(1, 3)
            if tmp_rand == 1:
                #double click
                if LorR == 'Left':
                    leftClick()
                    sleep(randint(43, 113) / 1000)
                    leftClick()
                else:
                    rightClick()
                    sleep(randint(43, 113) / 1000)
                    rightClick()

            elif tmp_rand == 2:
                if LorR == 'Left':
                    rightClick()

# Event.mouse_moving((1000, 400), 'Left')
