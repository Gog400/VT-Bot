from PIL import ImageGrab
import numpy as np
import pytesseract
import cv2

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"


originalImage = cv2.imread('Layer_2.png') # D:\Work\Programming\pyth\MMOrpg_bot\Character Recognition\Layer_1.png

h, w = originalImage.shape[:2]
originalImage = cv2.resize(originalImage, (w*5, h*5)) # (109,15)

grayImage = cv2.cvtColor(originalImage, cv2.COLOR_BGR2GRAY)
(thresh, blackAndWhiteImage) = cv2.threshold(grayImage, 127, 255, cv2.THRESH_BINARY)

cv2.imshow('Black white image', blackAndWhiteImage)
# cv2.imshow('Original image',originalImage)
# cv2.imshow('Gray image', grayImage)

text = pytesseract.image_to_string(blackAndWhiteImage, lang = 'eng')

print(text)
cv2.waitKey(0)
cv2.destroyAllWindows()
