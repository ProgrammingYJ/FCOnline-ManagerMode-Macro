import pyautogui as pgi
import time
import keyboard
import pydirectinput as pyd
import random
import os

print('해상도 1920*1080 FHD')
print('창모드 최대화 권장')
print('"F3" 시작 / "F4" 10초 누르면 종료')

width, height = pgi.size()
print('해상도 :', width, height)


def skey():
    pyd.keyDown("s")
    time.sleep(0.05)
    pyd.keyUp("s")


def imgclick(files):
    try:
        imgfile = pgi.locateCenterOnScreen(files, confidence=0.7)
        if imgfile == None:
            pass
        else:
            print(imgfile)
            print(f"{files}이미지 인식됐어요")
            x, y = imgfile
            x = x - random.randint(1, 20) + random.randint(1, 20)
            y = y - random.randint(1, 20) + random.randint(1, 20)
            pgi.click(x, y)
    except:
        pass

def skip_30s():
    pyd.keyDown("s")
    time.sleep(0.05)
    pyd.keyUp("s")

def skeypress(files):
    try:
        imgfile = pgi.locateCenterOnScreen(files, confidence=0.8)
        if imgfile == None:
            pass
        else:
            print(imgfile)
            print("s키 인식됐어요")
            x, y = imgfile
            x = x - random.randint(1, 20) + random.randint(1, 20)
            y = y - random.randint(1, 20) + random.randint(1, 20)
            pgi.click(x, y)
            pyd.keyDown("s")
            time.sleep(0.05)
            pyd.keyUp("s")
    except:
        pass


def esckeypress(files):
    try:
        imgfile = pgi.locateCenterOnScreen(files, confidence=0.8)
        if imgfile == None:
            pass
        else:
            print(imgfile)
            print("esc인식됐어요")
            x, y = imgfile
            x = x - random.randint(1, 20) + random.randint(1, 20)
            y = y - random.randint(1, 20) + random.randint(1, 20)
            pgi.click(x, y)
            pyd.keyDown("esc")
            time.sleep(0.05)
            pyd.keyUp("esc")
    except:
        pass

while True:
    if keyboard.is_pressed('F3'):
        print('작업시작')

        while True:
            if keyboard.is_pressed('F4'):
                print('중지됨')
                break
            else:
                esckeypress('esc2.png')
                skeypress('s.png')
                imgclick('og.png')
                imgclick('continue.png')
                imgclick('completedchoose.png')
                imgclick('next.png')
                imgclick('ok.png')
                skeypress('s.png')
                skip_30s()
                imgclick("ready.png")