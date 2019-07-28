from PIL import ImageGrab
import numpy as np
import cv2


screenCapture = ImageGrab.grab(bbox=(445, 203, 1477, 878)) # Grab only marketplace window
screenCapture_np = np.array(screenCapture)
screenCapture = cv2.cvtColor(screenCapture_np, cv2.COLOR_BGR2GRAY)
cv2.imshow("screenCapture", screenCapture)


cv2.waitKey(0)
cv2.destroyAllWindows()
