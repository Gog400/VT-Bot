from PIL import ImageGrab
import numpy as np
import cv2
import time
import pytesseract

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

## Установление предмета для поиска
template = cv2.imread('Functionality\Layer_2.png', cv2.IMREAD_GRAYSCALE)
w, h = template.shape[::-1]


def process_img(original_img):
    grey_img = cv2.cvtColor(original_img, cv2.COLOR_BGR2GRAY)
    (thresh, BnW_img) = cv2.threshold(grey_img, 127, 255, cv2.THRESH_BINARY)

    text = pytesseract.image_to_string(BnW_img, lang = 'eng')

    ## Нахождение предмета
    res = cv2.matchTemplate(grey_img, template, cv2.TM_CCOEFF_NORMED)
    loc = np.where( res >= 0.8)

    ## Обрисовка предмета
    for pt in zip(*loc[::-1]):
        cv2.rectangle(original_img, pt, (pt[0] + w, pt[1] + h), (204, 40, 142), 2)

    cv2.putText(original_img, str(text), (0,130), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 4)
    processed_imgs = [grey_img, BnW_img]
    return processed_imgs


last_time = time.time()
while True:
    # Захват экрана
    screen = np.array(ImageGrab.grab(bbox=(0, 40, 640, 360)))
    screen2 = process_img(screen)

    # Подсчет ФПС
    print('FPS: {}'.format(1 / (time.time()-last_time) ))
    last_time = time.time()

    cv2.imshow('Default screen', cv2.cvtColor(screen, cv2.COLOR_BGR2RGB))
    cv2.imshow('Processed screen', screen2[1])

    if cv2.waitKey(25) & 0xFF == ord('q'):
        cv2.destroyAllWindows()
        break
