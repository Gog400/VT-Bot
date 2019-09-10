from PIL import ImageGrab
import numpy as np
import cv2
import time
import pytesseract
from KeyboardEvents import PressKey, ReleaseKey, characters
from LineAlgorthm import Event
import datetime
from random import randint
from humanclicker import HumanClicker


pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

## Установление предмета для поиска
template = cv2.imread('Functionality\Axe1.png', cv2.IMREAD_GRAYSCALE)
w, h = template.shape[::-1]

hc = HumanClicker()

def writeText(text):
    # if __name__ == '__main__':
    global queue
    queue = text.upper()
    for c in queue:
        time.sleep(uniform(0.05, 0.15))
        PressKey(characters[c])
        print(c + ' pressed')
        time.sleep(uniform(0.05, 0.15))
        ReleaseKey(characters[c])
        print(c + ' released' + '\n')

    return queue

def CharRecogn(original_img, pt):
    # global priceArray
    # global recognizedText
    # priceArray = []

    zoom_screen = np.array(ImageGrab.grab(bbox=(pt[0], pt[1], pt[0]+w, pt[1]+h)))
    zoom_screen = cv2.resize(zoom_screen, (w*5, h*5))
    zoom_screen_grey = cv2.cvtColor(zoom_screen, cv2.COLOR_BGR2GRAY)
    (thresh, BnW_img) = cv2.threshold(zoom_screen_grey, 127, 255, cv2.THRESH_BINARY)
    recognizedText = pytesseract.image_to_string(BnW_img, lang = 'eng')
    cv2.putText(original_img, str(recognizedText), (pt[0]+w, pt[1]+h), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 2)

    return original_img

def dataStamp(file, header, unitPrice):
    f = open(file, 'w')
    f.write(datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S') + ' | ' + header +' | '+ unitPrice + '\n')
    f.close()

def process_img(original_img):

    grey_img = cv2.cvtColor(original_img, cv2.COLOR_BGR2GRAY)

    ## Нахождение предмета
    res = cv2.matchTemplate(grey_img, template, cv2.TM_CCOEFF_NORMED)
    loc = np.where( res >= 0.8)
    loc_n = list(zip(*loc[::-1]))


    try:

        bottom_rect = [ [loc_n[0][0]+ w//2 - 10, loc_n[0][1]+95], [loc_n[0][0] + w//2 + 10, loc_n[0][1] + 115] ]

        bottom_rect_h = bottom_rect[1][1] - bottom_rect[0][1]
        bottom_rect_w = bottom_rect[1][0] - bottom_rect[0][0]

        cv2.putText(original_img,'X: %d | Y: %d' % (loc_n[0][0], loc_n[0][1]) , (loc_n[0][0]+w+5, loc_n[0][1]+h-3), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 2)

        cv2.rectangle(original_img, loc_n[0], (loc_n[0][0] + w, loc_n[0][1] + h), (204, 40, 142), 2)
        cv2.rectangle(original_img, (bottom_rect[0][0], bottom_rect[0][1]), (bottom_rect[1][0], bottom_rect[1][1]), (204, 40, 255), 2)

        i = randint(0, 10)
        if i == 1:
            rectrandX = randint(bottom_rect[0][0], bottom_rect[0][0] + bottom_rect_w)
            rectrandY = randint(bottom_rect[0][1], bottom_rect[0][1] + bottom_rect_h)

            cv2.circle(original_img, (rectrandX, rectrandY), 1, (220, 20, 60), thickness = 3)

            hc.move((rectrandX+10, rectrandY+30), 1)
            # hc.rightClick()
            # hc.real_click('Right') # Походу придется переписывать код (полностью(кириллу)), также походу код перегружен и ивент клика тупо не запускается. Походу придеться делать многопоток


            # WriteText('r')

            # print('Y1 ',bottom_rect[0][1])
            # print('Y2 ',bottom_rect[1][1])
            # Event.mouse_moving((rectrandX+10, rectrandY+30), 'Left')

    except:
        pass



    ## Обрисовка предмета
    # for pt in zip(*loc[::-1]):
    #     cv2.rectangle(original_img, pt, (pt[0] + w, pt[1] + h), (204, 40, 142), 2)
    #     # original_img = CharRecogn(original_img, pt)
    #
    #     # Квадрат аима на перса
    #     cv2.rectangle(original_img, (pt[0]+ w//2 - 10, pt[1]+95), (pt[0] + w//2 + 10, pt[1] + 115), (204, 40, 255), 2)

    return grey_img

# def canny(original_img):
#      original_img = cv2.Canny(cv2.cvtColor(original_img, cv2.COLOR_BGR2GRAY), 200, 300)
#      return original_img



## Обратный отсчет
for i in list(range(3))[::-1]:
    print(i+1)
    time.sleep(1)

# writeText("Titan's treasure")
# Event.mouse_moving((300,300))


last_time = time.time()
while True:
    # Захват экрана
    # screen = np.array(ImageGrab.grab(bbox=(0, 0, 960, 1080))) # Right half of monitor
    screen = np.array(ImageGrab.grab(bbox=(0, 0, 1920, 1080))) # Right half of monitor
    screen2 = process_img(screen)
    # screen3 = canny(screen)

    # Подсчет ФПС
    # print('FPS: {}'.format(1 / (time.time()-last_time) ))
    cv2.putText(screen, 'FPS: {}'.format(int(1 / (time.time()-last_time))), (0, 1000), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
    last_time = time.time()

    # cv2.imshow('Default screen', cv2.cvtColor(screen, cv2.COLOR_BGR2RGB))
    # cv2.imshow('Template', template)

    # cv2.imshow('Processed screen', screen2)

    # try:
    #     if recognizedText not in priceArray:
    #         priceArray.append(recognizedText)# Массив почему-то постоянно обновляется, я не знаю почему. Также, непонятно как recognizedText себя
    #         # ведет, когда несколько цен определяются одновременно. Скорее всего придется вручную настрить захват окон с ценами
    #
    #     for i in priceArray:
    #         dataStamp('CollectedData.py', "Titan's treasure", i)
    # except:
    #     pass
    if cv2.waitKey(25) & 0xFF == ord('q'):
        cv2.destroyAllWindows()
        break
