from PIL import ImageGrab
import numpy as np
import cv2
import time
import pytesseract
from test2 import PressKey, ReleaseKey, characters

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

## Установление предмета для поиска
template = cv2.imread('Functionality\Layer_2.png', cv2.IMREAD_GRAYSCALE)
w, h = template.shape[::-1]


def writeText(text):
    # if __name__ == '__main__':
    queue = text.upper()
    for c in queue:
        time.sleep(0.1)
        PressKey(characters[c])
        print(c + ' pressed')
        time.sleep(0.1)
        ReleaseKey(characters[c])
        print(c + ' released' + '\n')

def CharRecogn(original_img, pt):
    zoom_screen = np.array(ImageGrab.grab(bbox=(pt[0], pt[1], pt[0]+w, pt[1]+h)))
    zoom_screen = cv2.resize(zoom_screen, (w*5, h*5))
    zoom_screen_grey = cv2.cvtColor(zoom_screen, cv2.COLOR_BGR2GRAY)
    (thresh, BnW_img) = cv2.threshold(zoom_screen_grey, 127, 255, cv2.THRESH_BINARY)
    text = pytesseract.image_to_string(BnW_img, lang = 'eng')
    cv2.putText(original_img, str(text), (pt[0]+w, pt[1]+h), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 2)
    return original_img

def process_img(original_img):
    grey_img = cv2.cvtColor(original_img, cv2.COLOR_BGR2GRAY)

    ## Нахождение предмета
    res = cv2.matchTemplate(grey_img, template, cv2.TM_CCOEFF_NORMED)
    loc = np.where( res >= 0.8)

    ## Обрисовка предмета
    for pt in zip(*loc[::-1]):
        cv2.rectangle(original_img, pt, (pt[0] + w, pt[1] + h), (204, 40, 142), 2)
        original_img = CharRecogn(original_img, pt)

    return grey_img

## Обратный отсчет
for i in list(range(3))[::-1]:
    print(i+1)
    time.sleep(1)

writeText("Titan's treasure")

last_time = time.time()
while True:
    # Захват экрана
    screen = np.array(ImageGrab.grab(bbox=(0, 0, 640, 360)))
    screen2 = process_img(screen)

    # Подсчет ФПС
    # print('FPS: {}'.format(1 / (time.time()-last_time) ))
    last_time = time.time()

    cv2.imshow('Default screen', cv2.cvtColor(screen, cv2.COLOR_BGR2RGB))
    cv2.imshow('Processed screen', screen2)

    if cv2.waitKey(25) & 0xFF == ord('q'):
        cv2.destroyAllWindows()
        break
