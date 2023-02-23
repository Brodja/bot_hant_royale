from glob import glob
import cv2
import pyautogui
import pyscreenshot as ImageGrab
import time
import keyboard

START_POSITION_X = 0
START_POSITION_Y = 0

def findStartPosition():
  global START_POSITION_X, START_POSITION_Y
  ImageGrab.grab().save('screenshot.png')
  result = cv2.matchTemplate(cv2.imread('screenshot.png'), cv2.imread('./image/blueStacksIcon.png'), cv2.TM_CCOEFF_NORMED)
  (min_x, max_y, minloc, maxloc) = cv2.minMaxLoc(result)
  START_POSITION_X = maxloc[0]
  START_POSITION_Y = maxloc[1]
  pyautogui.moveTo(START_POSITION_X, START_POSITION_Y)

def pressStartGame():
  global START_POSITION_X, START_POSITION_Y
  pyautogui.click(START_POSITION_X + 270, START_POSITION_Y + 800)

def searchArenaLine():  
  ImageGrab.grab().save('screenshot.png')
  result = cv2.matchTemplate(cv2.imread('screenshot.png'), cv2.imread('./image/arenaLine.png'), cv2.TM_CCOEFF_NORMED)
  (min_x, max_y, minloc, maxloc) = cv2.minMaxLoc(result)
  print(min_x, max_y, minloc, maxloc)
  pyautogui.moveTo(maxloc[0], maxloc[1])

def moveHeroToArena():
  global START_POSITION_X, START_POSITION_Y
  pyautogui.moveTo(START_POSITION_X + 260, START_POSITION_Y + 825)
  pyautogui.mouseDown()
  pyautogui.moveTo(START_POSITION_X + 320, START_POSITION_Y + 760)
  time.sleep(2.5)
  pyautogui.mouseUp()

def run(count):    
  time.sleep(2)
  print(count)
  findStartPosition()
  # searchArenaLine()
  moveHeroToArena()

if __name__=="__main__":
    run(1)  