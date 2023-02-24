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
  pyautogui.moveTo(START_POSITION_X, START_POSITION_Y)

def pressStartGame():
  global START_POSITION_X, START_POSITION_Y
  pyautogui.click(START_POSITION_X + 270, START_POSITION_Y + 800)

def awaitGameArena():
  screenFull()
  result = cv2.matchTemplate(cv2.imread('screenshot.png'), cv2.imread('./image/game_pult.png'), cv2.TM_CCOEFF_NORMED)
  (min_x, max_y, minloc, maxloc) = cv2.minMaxLoc(result)
  print('awaitGameArena', max_y)
  if  max_y < 0.98:
     time.sleep(3)
     awaitGameArena()


def checkMyPosition():
  screenFull()
  result = cv2.matchTemplate(cv2.imread('screenshot.png'), cv2.imread('./image/healt_field.png'), cv2.TM_CCOEFF_NORMED)
  (min_x, max_y, minloc, maxloc) = cv2.minMaxLoc(result)
  print('checkMyPosition', max_y)
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
  if  max_y < 0.98:
     time.sleep(5)
     checkKillBoss()

def pickHero(hero):
  pyautogui.moveTo(START_POSITION_X + 300, START_POSITION_Y + 400)
  screenFull()
  result = cv2.matchTemplate(cv2.imread('screenshot.png'), cv2.imread('./image/' + str(hero) + '.png'), cv2.TM_CCOEFF_NORMED)
  (min_x, max_y, minloc, maxloc) = cv2.minMaxLoc(result) 
  print('pickHero', hero, max_y)
  if  max_y < 0.95: 
    pyautogui.scroll(-100)  
    time.sleep(1) 
    pickHero(hero)
  else:
      pyautogui.click(maxloc[0] + 10, maxloc[1] + 10)
      time.sleep(0.5) 
      pyautogui.click(START_POSITION_X + 380, START_POSITION_Y + 815)

def closeTotal():
  screenFull()
  result = cv2.matchTemplate(cv2.imread('screenshot.png'), cv2.imread('./image/total.png'), cv2.TM_CCOEFF_NORMED)
  (min_x, max_y, minloc, maxloc) = cv2.minMaxLoc(result)
  print('closeTotal', max_y)
  if  max_y < 0.98: 
    time.sleep(5) 
    closeTotal()
  else:
    pyautogui.click(maxloc[0] + 3, maxloc[1] + 3)
    time.sleep(1) 
    pyautogui.click(maxloc[0] + 3, maxloc[1] + 3)

def checkAndClose15():
  screenFull()
  result = cv2.matchTemplate(cv2.imread('screenshot.png'), cv2.imread('./image/pickHero.png'), cv2.TM_CCOEFF_NORMED)
  (min_x, max_y, minloc, maxloc) = cv2.minMaxLoc(result)
  print('checkAndClose15', max_y)
  if  max_y > 0.98:
    pickHero(12)

def checkAndPickBonus():
  screenFull()
  result = cv2.matchTemplate(cv2.imread('screenshot.png'), cv2.imread('./image/get_bonus.png'), cv2.TM_CCOEFF_NORMED)
  (min_x, max_y, minloc, maxloc) = cv2.minMaxLoc(result)
  print(max_y)
  if  max_y > 0.98:
    pyautogui.click(maxloc[0] + 150, maxloc[1] + 140)
    time.sleep(0.5)
    pyautogui.click(maxloc[0] + 150, maxloc[1] + 140)
    time.sleep(0.5)
    pyautogui.click(maxloc[0] + 150, maxloc[1] + 140)

def exit():
  screenFull()
  result = cv2.matchTemplate(cv2.imread('screenshot.png'), cv2.imread('./image/exit.png'), cv2.TM_CCOEFF_NORMED)
  (min_x, max_y, minloc, maxloc) = cv2.minMaxLoc(result)
  print(max_y)
  if  max_y > 0.98:
    pyautogui.click(maxloc[0] + 20, maxloc[1] + 10)
    time.sleep(10)
    pyautogui.click(START_POSITION_X + 270, START_POSITION_Y + 270)
  else:
    time.sleep(1)
    exit()

def checkReloadGems():   
  screenFull()
  result = cv2.matchTemplate(cv2.imread('screenshot.png'), cv2.imread('./image/reload_gems.png'), cv2.TM_CCOEFF_NORMED)
  (min_x, max_y, minloc, maxloc) = cv2.minMaxLoc(result)
  print(max_y)
  if  max_y > 0.98:
    pyautogui.click(maxloc[0] + 20, maxloc[1] + 10) 


def run(count):  
  time.sleep(3)
  findStartPosition()
  for num in range(1,count):
    pressStartGame()
    time.sleep(1)
    checkReloadGems()
    awaitGameArena()
    disconnect()
    checkMyPosition()
    moveHeroToArena()
    checkKillBoss()
    for hero in range(12,21):
      pickHero(hero)
      awaitGameArena()
      checkMyPosition()
      moveHeroToArena()
      if hero < 21:
        checkKillBoss()
  closeTotal()
  time.sleep(1)
  checkAndClose15()
  time.sleep(1)
  checkAndPickBonus()
  time.sleep(1)
  exit()


if __name__=="__main__":
    run(3)  

