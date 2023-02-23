from glob import glob
import cv2
import pyautogui
import pyscreenshot as ImageGrab
import time
import keyboard

START_POSITION_X = 0
START_POSITION_Y = 0

def screenFull():
  ImageGrab.grab(bbox=(1, 1, 1900, 1000)).save('screenshot.png')

def disconnect():
  pyautogui.keyDown('ctrl')
  pyautogui.keyDown('shift')
  pyautogui.press('h')
  time.sleep(2)
  pyautogui.press('h') 
  pyautogui.keyUp('ctrl')
  pyautogui.keyUp('shift')


def findStartPosition():
  global START_POSITION_X, START_POSITION_Y
  screenFull()
  result = cv2.matchTemplate(cv2.imread('screenshot.png'), cv2.imread('./image/blueStacksIcon.png'), cv2.TM_CCOEFF_NORMED)
  (min_x, max_y, minloc, maxloc) = cv2.minMaxLoc(result)
  START_POSITION_X = maxloc[0]
  START_POSITION_Y = maxloc[1]
  print('findStartPosition', START_POSITION_X, START_POSITION_Y)
  pyautogui.moveTo(START_POSITION_X, START_POSITION_Y)

def pressStartGame():
  global START_POSITION_X, START_POSITION_Y
  pyautogui.click(START_POSITION_X + 270, START_POSITION_Y + 800)

def awaitGameArena():
  screenFull()
  result = cv2.matchTemplate(cv2.imread('screenshot.png'), cv2.imread('./image/game_pult.png'), cv2.TM_CCOEFF_NORMED)
  (min_x, max_y, minloc, maxloc) = cv2.minMaxLoc(result)
  if  max_y > 0.98:
    print('Нашел')
  else:  
     print('Не нашел')
     time.sleep(3)
     awaitGameArena()


def checkMyPosition():
  screenFull()
  result = cv2.matchTemplate(cv2.imread('screenshot.png'), cv2.imread('./image/healt_field.png'), cv2.TM_CCOEFF_NORMED)
  (min_x, max_y, minloc, maxloc) = cv2.minMaxLoc(result)
  print('checkMyPosition', min_x, max_y, minloc, maxloc)
  if  max_y > 0.9:
    if maxloc[0] > 300:
      moveDown()

def moveDown():
  global START_POSITION_X, START_POSITION_Y
  pyautogui.moveTo(START_POSITION_X + 260, START_POSITION_Y + 825)
  pyautogui.mouseDown()
  pyautogui.moveTo(START_POSITION_X + 320, START_POSITION_Y + 895)
  time.sleep(0.2)
  pyautogui.mouseUp()

def moveHeroToArena():
  global START_POSITION_X, START_POSITION_Y
  pyautogui.moveTo(START_POSITION_X + 260, START_POSITION_Y + 825)
  pyautogui.mouseDown()
  pyautogui.moveTo(START_POSITION_X + 320, START_POSITION_Y + 755)
  time.sleep(2.5)
  pyautogui.mouseUp()

def checkKillBoss():
  screenFull()
  result = cv2.matchTemplate(cv2.imread('screenshot.png'), cv2.imread('./image/pickHero.png'), cv2.TM_CCOEFF_NORMED)
  (min_x, max_y, minloc, maxloc) = cv2.minMaxLoc(result)
  if  max_y > 0.98:
    print('Убил босса')
  else:  
     print('Не убил')
     time.sleep(5)
     checkKillBoss()

def pickHero(hero):
  pyautogui.click(START_POSITION_X + 300, START_POSITION_Y + 400)
  screenFull()
  result = cv2.matchTemplate(cv2.imread('screenshot.png'), cv2.imread('./image/' + str(hero) + '.png'), cv2.TM_CCOEFF_NORMED)
  (min_x, max_y, minloc, maxloc) = cv2.minMaxLoc(result) 
  if  max_y < 0.98: 
    pyautogui.scroll(-50)  
    time.sleep(1) 
    pickHero(hero)
  else:
      pyautogui.click(maxloc[0], maxloc[1])
      time.sleep(0.5) 
      pyautogui.click(START_POSITION_X + 380, START_POSITION_Y + 815)


def run(count):  
  time.sleep(3)
  findStartPosition()
  pressStartGame()
  awaitGameArena()
  disconnect()
  checkMyPosition()
  moveHeroToArena()
  checkKillBoss()
  for hero in range(2,20):
    pickHero(hero)
    awaitGameArena()
    checkMyPosition()
    moveHeroToArena()
    checkKillBoss()


if __name__=="__main__":
    run(1)  

# def searchArenaLine():  
#   screenFull()
#   result = cv2.matchTemplate(cv2.imread('screenshot.png'), cv2.imread('./image/arenaLine.png'), cv2.TM_CCOEFF_NORMED)
#   (min_x, max_y, minloc, maxloc) = cv2.minMaxLoc(result)
#   print(min_x, max_y, minloc, maxloc)
#   pyautogui.moveTo(maxloc[0], maxloc[1])