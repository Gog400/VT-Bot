from PIL import ImageGrab
import numpy as np
import cv2
import time


template = cv2.imread('Layer_2.png', cv2.IMREAD_GRAYSCALE)
w, h = template.shape[::-1]


screen = cv2.imread('Layer_0.png')
screen2 = cv2.cvtColor(screen, cv2.COLOR_BGR2GRAY)


res = cv2.matchTemplate(screen2, template, cv2.TM_CCOEFF_NORMED)
loc = np.where( res >= 0.8)
for pt in zip(*loc[::-1]):
    cv2.rectangle(screen, pt, (pt[0] + w, pt[1] + h), (0,0,255), 2)

cv2.imshow('Detected', screen)
