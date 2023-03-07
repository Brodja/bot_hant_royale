from glob import glob
import cv2
import pyautogui
import pyscreenshot as ImageGrab
import time
import keyboard

START_POSITION_X = 0
START_POSITION_Y = 0
# Получить позицию окна
def screenFull():
  ImageGrab.grab(bbox=(1, 1, 1900, 1000)).save('screenshot.png')

# Поск своей позиции при старте первого уровня (пока для Ети)
def findStartPosition():
  global START_POSITION_X, START_POSITION_Y
  screenFull()
  result = cv2.matchTemplate(cv2.imread('screenshot.png'), cv2.imread('./image/blueStacksIcon.png'), cv2.TM_CCOEFF_NORMED)
  (min_x, max_y, minloc, maxloc) = cv2.minMaxLoc(result)
  START_POSITION_X = maxloc[0]
  START_POSITION_Y = maxloc[1]
  pyautogui.moveTo(START_POSITION_X, START_POSITION_Y)
  print('START_POSITION_X', START_POSITION_X, 'START_POSITION_Y', START_POSITION_Y)
# Клик запуска игры
def pressStartGame():
  global START_POSITION_X, START_POSITION_Y
  pyautogui.click(START_POSITION_X + 270, START_POSITION_Y + 800)
  print('Start game was pressed')

# Проверка на окно с токенами
def checkReloadGems():   
  screenFull()
  result = cv2.matchTemplate(cv2.imread('screenshot.png'), cv2.imread('./image/reload_gems.png'), cv2.TM_CCOEFF_NORMED)
  (min_x, max_y, minloc, maxloc) = cv2.minMaxLoc(result)
  print(max_y)
  if  max_y > 0.98:
    pyautogui.click(maxloc[0] + 20, maxloc[1] + 10)   
  print('Checked new tokens')  

# Ожидание игрового поля
def awaitGameArena(path):
  print('Start find game field') 
  screenFull()
  result = cv2.matchTemplate(cv2.imread('screenshot.png'), cv2.imread(path), cv2.TM_CCOEFF_NORMED)
  (min_x, max_y, minloc, maxloc) = cv2.minMaxLoc(result)
  print('awaitGameArena', max_y)
  if  max_y < 0.95:
     time.sleep(2)
     awaitGameArena(path)
  else:   
    print('Game field finded')   

# Разорвать соединение
def disconnect():
  pyautogui.keyDown('ctrl')
  pyautogui.keyDown('shift')
  pyautogui.press('h')
  time.sleep(2)
  pyautogui.press('h') 
  pyautogui.keyUp('ctrl')
  pyautogui.keyUp('shift')
  print('Disconnected')

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
  print('Пришел')

# Перемещение к кракену
def moveToKraken():
  time.sleep(3)
  pyautogui.keyDown('w')
  pyautogui.keyDown('d')
  time.sleep(0.35)
  pyautogui.keyUp('d')
  time.sleep(0.15)
  pyautogui.keyUp('w')
  print('Moved to kraken')

# Проверка на убийство босса
def checkKillBoss():
  screenFull()
  result = cv2.matchTemplate(cv2.imread('screenshot.png'), cv2.imread('./image/pickHero.png'), cv2.TM_CCOEFF_NORMED)
  (min_x, max_y, minloc, maxloc) = cv2.minMaxLoc(result)
  print('checkKillBoss', max_y)
  if  max_y < 0.98:
     time.sleep(5)
     checkKillBoss()
  else:
    print('Boss killed')   

# Выбор героя
def pickHero(path, hero):
  pyautogui.moveTo(START_POSITION_X + 300, START_POSITION_Y + 400)
  screenFull()
  result = cv2.matchTemplate(cv2.imread('screenshot.png'), cv2.imread(path), cv2.TM_CCOEFF_NORMED)
  (min_x, max_y, minloc, maxloc) = cv2.minMaxLoc(result) 
  print('pickHero', hero, max_y)
  if  max_y < 0.95: 
    pyautogui.scroll(-100)  
    time.sleep(1) 
    pickHero(path, hero)
  else:
      pyautogui.click(maxloc[0] + 10, maxloc[1] + 10)
      time.sleep(0.5) 
      pyautogui.click(START_POSITION_X + 380, START_POSITION_Y + 815)

# получить награду
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

# добавить бонусс
def checkAndClose15():
  screenFull()
  result = cv2.matchTemplate(cv2.imread('screenshot.png'), cv2.imread('./image/pickHero.png'), cv2.TM_CCOEFF_NORMED)
  (min_x, max_y, minloc, maxloc) = cv2.minMaxLoc(result)
  print('checkAndClose15', max_y)
  if  max_y > 0.98:
    pickHero('./kraken_image/' + str(14) + '.png', 14)

def checkAndPickBonus(path):
  screenFull()
  # './yeti_image/get_bonus.png'
  result = cv2.matchTemplate(cv2.imread('screenshot.png'), cv2.imread(path), cv2.TM_CCOEFF_NORMED)
  (min_x, max_y, minloc, maxloc) = cv2.minMaxLoc(result)
  print(max_y)
  if  max_y > 0.98:
    pyautogui.click(maxloc[0] + 150, maxloc[1] + 140)
    time.sleep(0.5)
    pyautogui.click(maxloc[0] + 150, maxloc[1] + 140)
    time.sleep(0.5)
    pyautogui.click(maxloc[0] + 150, maxloc[1] + 140)

def exitGame():
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
    exitGame()

def skipKrakenFarm():
  pyautogui.click(START_POSITION_X + 260, START_POSITION_Y + 130)
  time.sleep(0.5)
  pyautogui.click(START_POSITION_X + 350, START_POSITION_Y + 625)
  print('skipKrakenFarm')

