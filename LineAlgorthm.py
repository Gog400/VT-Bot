import win32gui, win32api, win32con, ctypes
from time import sleep
from random import uniform

def get_line(start, end):
    """Bresenham's Line Algorithm
    Produces a list of tuples from start and end

    >>> points1 = get_line((0, 0), (3, 4))
    >>> points2 = get_line((3, 4), (0, 0))
    >>> assert(set(points1) == set(points2))
    >>> print points1
    [(0, 0), (1, 1), (1, 2), (2, 3), (3, 4)]
    >>> print points2
    [(3, 4), (2, 3), (1, 2), (1, 1), (0, 0)]
    """
    # Setup initial conditions
    x1, y1 = start
    x2, y2 = end
    dx = x2 - x1
    dy = y2 - y1

    # Determine how steep the line is
    is_steep = abs(dy) > abs(dx)

    # Rotate line
    if is_steep:
        x1, y1 = y1, x1
        x2, y2 = y2, x2

    # Swap start and end points if necessary and store swap state
    swapped = False
    if x1 > x2:
        x1, x2 = x2, x1
        y1, y2 = y2, y1
        swapped = True

    # Recalculate differentials
    dx = x2 - x1
    dy = y2 - y1

    # Calculate error
    error = int(dx / 2.0)
    ystep = 1 if y1 < y2 else -1

    # Iterate over bounding box generating points between start and end
    y = y1
    points = []
    for x in range(x1, x2 + 1):
        coord = (y, x) if is_steep else (x, y)
        points.append(coord)
        error -= abs(dy)
        if error < 0:
            y += ystep
            error += dx

    # Reverse the list if the coordinates were swapped
    if swapped:
        points.reverse()
    return points


class Event():

    def pos(x, y):
        ctypes.windll.user32.SetCursorPos(x, y)

    def leftClick():
        ctypes.windll.user32.mouse_event(2, 0, 0, 0,0) # left down
        sleep(uniform(0.05, 0.15))
        ctypes.windll.user32.mouse_event(4, 0, 0, 0,0) # left up

    def rightClick():
        ctypes.windll.user32.mouse_event(8, 0, 0, 0,0) # Right down
        sleep(uniform(0.05, 0.15))
        ctypes.windll.user32.mouse_event(10, 0, 0, 0,0) # Right up


    def mouse_moving(end, button):


        start = win32api.GetCursorPos()

        points1 = get_line(start, end)

        S = (len(points1)-1) / 2
        # see http://msdn.microsoft.com/en-us/library/ms646260(VS.85).aspx for details

        for p in points1:
            delay = uniform(0.0003, 0.0007) # 0.0005
            Event.pos(p[0], p[1])
            sleep(delay)

            if p == points1[len(points1)-1]:

                if button == 'Left':
                    Event.leftClick()

                elif button == 'Right':
                    Event.rightClick()

# Event.mouse_moving((1000, 400), 'Left')
