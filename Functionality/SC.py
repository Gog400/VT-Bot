from PIL import ImageGrab
import numpy as np
import cv2
import time

## Установление предмета для поиска
template = cv2.imread('Layer_2.png', cv2.IMREAD_GRAYSCALE)
w, h = template.shape[::-1]


def process_img(original_img):
    processed_img = cv2.cvtColor(original_img, cv2.COLOR_BGR2GRAY)

    ## Нахождение предмета
    res = cv2.matchTemplate(processed_img, template, cv2.TM_CCOEFF_NORMED)
    loc = np.where( res >= 0.8)

    ## Обрисовка предмета
    for pt in zip(*loc[::-1]):
        cv2.rectangle(original_img, pt, (pt[0] + w, pt[1] + h), (204, 40, 142), 2)
    return processed_img


last_time = time.time()
while True:
    # Захват экрана
    screen = np.array(ImageGrab.grab(bbox=(0, 40, 640, 360)))
    screen2 = process_img(screen)

    # Подсчет ФПС
    print('FPS: {}'.format(1 / (time.time()-last_time) ))
    last_time = time.time()

    cv2.imshow('Default screen', cv2.cvtColor(screen, cv2.COLOR_BGR2RGB))
    # cv2.imshow('Processed screen', screen2)

    if cv2.waitKey(25) & 0xFF == ord('q'):
        cv2.destroyAllWindows()
        break
