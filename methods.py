from glob import glob
import cv2
import pyautogui
import pyscreenshot as ImageGrab
import time
import keyboard
import yeti
import kraken
import chaos

START_POSITION_X = 0
START_POSITION_Y = 0
lastUpdate = time.time()
running = True

def restart():
  # Перезапуск гри
    restartHuntRoyale()
    # yeti.startYetiLogic()
    # kraken.startKrakenLogic()
    chaos.startChaosLogic()
    
def checkLag():
  global lastUpdate, running 
  print('check lag', time.time() - lastUpdate)
  if running == False:
    print('Stop logic')
    return
  if (time.time() - lastUpdate > 200):
    print('Помилка в алгоритмі, необхідний перезапуск')
    return restart()


# Запуск емулятору
def launchEmulator():
  doScreenshot(True)
  result = cv2.matchTemplate(cv2.imread('screenshot.png'), cv2.imread('./image/emulator_icon.png'), cv2.TM_CCOEFF_NORMED)
  (min_x, max_y, minloc, maxloc) = cv2.minMaxLoc(result)
  pyautogui.click(maxloc[0] + 30, maxloc[1] + 30, clicks=2)

# Очікування завантаження
def awaitLaunchEmulator():
  doScreenshot(True)
  result = cv2.matchTemplate(cv2.imread('screenshot.png'), cv2.imread('./image/emulator_deck.png'), cv2.TM_CCOEFF_NORMED)
  (min_x, max_y, minloc, maxloc) = cv2.minMaxLoc(result)
  print('Очікування завантаження емулятора', max_y)
  if  max_y > 0.9:
    print('Емулятор завантажено')
  else:
    time.sleep(3)
    awaitLaunchEmulator()

# Перезапуск гри
def restartHuntRoyale():
  pyautogui.keyDown('ctrl')
  pyautogui.keyDown('shift')
  pyautogui.press('5')
  pyautogui.keyUp('ctrl')
  pyautogui.keyUp('shift')
  print('Меню відкрито') 
  time.sleep(1)
  doScreenshot(True)
  result = cv2.matchTemplate(cv2.imread('screenshot.png'), cv2.imread('./image/close_game_btn.png'), cv2.TM_CCOEFF_NORMED)
  (min_x, max_y, minloc, maxloc) = cv2.minMaxLoc(result)
  pyautogui.click(maxloc[0] + 25, maxloc[1] + 25)
  time.sleep(2)
  doScreenshot(True)
  result = cv2.matchTemplate(cv2.imread('screenshot.png'), cv2.imread('./image/game_icon.png'), cv2.TM_CCOEFF_NORMED)
  (min_x, max_y, minloc, maxloc) = cv2.minMaxLoc(result)
  pyautogui.click(maxloc[0] + 25, maxloc[1] + 25)

# Скрін екрану
def doScreenshot(mod=False):
  # Якщо true то усього екрану, інакше частину  
  if (mod):
    pyautogui.screenshot(region=(0, 0, 1920,  1040)).save('screenshot.png')
  else:
    pyautogui.screenshot(region=(START_POSITION_X, START_POSITION_Y, 560,  960)).save('screenshot.png')


# Пошук положення емулятору
def findPositionEmulator():
  global START_POSITION_X, START_POSITION_Y
  # Роблю знімок всього екрану
  doScreenshot(True)
  # Шукаю іконку
  result = cv2.matchTemplate(cv2.imread('screenshot.png'), cv2.imread('./image/blueStacksIcon.png'), cv2.TM_CCOEFF_NORMED)
  (min_x, max_y, minloc, maxloc) = cv2.minMaxLoc(result)
  # Присвоюю координати іконки
  START_POSITION_X = maxloc[0]
  START_POSITION_Y = maxloc[1]
  # Переміщую мишку до початку
  pyautogui.moveTo(START_POSITION_X, START_POSITION_Y)
  print('START_POSITION_X', START_POSITION_X, 'START_POSITION_Y', START_POSITION_Y)

def checkShop():
  global START_POSITION_X, START_POSITION_Y
  checkLag()
  doScreenshot()
  result = cv2.matchTemplate(cv2.imread('screenshot.png'), cv2.imread('./image/no.png'), cv2.TM_CCOEFF_NORMED)
  (min_x, max_y, minloc, maxloc) = cv2.minMaxLoc(result)
  print('Пошук магазину', max_y)
  if  max_y > 0.9:
    print('Закрить магазин')
    pyautogui.click(START_POSITION_X + maxloc[0] + 20, START_POSITION_Y + maxloc[1] + 10) 

# Клік на кнопку старт
def pressStartGame():
  global START_POSITION_X, START_POSITION_Y
  findPositionEmulator()
  checkShop()
  doScreenshot()
  result = cv2.matchTemplate(cv2.imread('screenshot.png'), cv2.imread('./image/start_game.png'), cv2.TM_CCOEFF_NORMED)
  (min_x, max_y, minloc, maxloc) = cv2.minMaxLoc(result)
  print('Пошук кнопки старт', max_y)
  if  max_y > 0.9:
    print('Клік на кнопку старт')
    pyautogui.click(START_POSITION_X + 270, START_POSITION_Y + 800)
  else:
    pyautogui.click(START_POSITION_X + 270, START_POSITION_Y + 270)
    time.sleep(3)
    pressStartGame()

# Перевірка оновлення токенів
def checkReloadGems():   
  doScreenshot()
  result = cv2.matchTemplate(cv2.imread('screenshot.png'), cv2.imread('./image/reload_gems.png'), cv2.TM_CCOEFF_NORMED)
  (min_x, max_y, minloc, maxloc) = cv2.minMaxLoc(result)
  if  max_y > 0.98:
    pyautogui.click(START_POSITION_X + maxloc[0] + 20, START_POSITION_Y + maxloc[1] + 10) 
  print('Перевірка на оновлення токенів завершена')    

# Очікування завантаження рівня та розрив інтернету
def awaitFindUserAndDisconnect():
  doScreenshot()
  result = cv2.matchTemplate(cv2.imread('screenshot.png'), cv2.imread('./image/load_game.png'), cv2.TM_CCOEFF_NORMED)
  (min_x, max_y, minloc, maxloc) = cv2.minMaxLoc(result)
  print('Пошук напарника', max_y)
  if  max_y < 0.8:
    print('Напарник знайдений')
    disconnect()
  else:
    time.sleep(1)
    awaitFindUserAndDisconnect()

# Розорив інтернету
def disconnect():
  pyautogui.keyDown('ctrl')
  pyautogui.keyDown('shift')
  pyautogui.press('h')
  time.sleep(1)
  pyautogui.press('h') 
  pyautogui.keyUp('ctrl')
  pyautogui.keyUp('shift')
  print('Зв\'язок з інтернером розірвано')    

# Перевірка на завантаження рівня кракена
def awaitLoadKrakenLvl():
  checkLag()
  doScreenshot()
  result = cv2.matchTemplate(cv2.imread('screenshot.png'), cv2.imread('./kraken_image/skip_farm.png'), cv2.TM_CCOEFF_NORMED)
  (min_x, max_y, minloc, maxloc) = cv2.minMaxLoc(result)
  print('Очікування завантаження рівня', max_y)
  if  max_y < 0.99999:
    print('Не готово')
    time.sleep(1)
    awaitLoadKrakenLvl()
  else:
    print('Рівень завантажено')

# Очікування повного завантаження корабля
def awaitKrakenShip():
  path = './kraken_image/kraken_ship3.png'
  doScreenshot()
  result = cv2.matchTemplate(cv2.imread('screenshot.png'), cv2.imread(path), cv2.TM_CCOEFF_NORMED)
  (min_x, max_y, minloc, maxloc) = cv2.minMaxLoc(result)
  print('Пошук завантаження корабля кракена', max_y)
  if  max_y < 0.8:
    time.sleep(1)
    awaitKrakenShip()
  else:   
    print('Корабель кракена завантажено') 

# Очікування смерті боса
def checkKillBoss():
  checkLag()
  doScreenshot()
  result = cv2.matchTemplate(cv2.imread('screenshot.png'), cv2.imread('./image/pickHero.png'), cv2.TM_CCOEFF_NORMED)
  (min_x, max_y, minloc, maxloc) = cv2.minMaxLoc(result)
  if  max_y < 0.98:
     time.sleep(3)
     checkKillBoss()
  else:
    print('Бос вбитий') 

# Вибір героя
def pickHero(type, hero):
  checkLag()
  if type == 'kraken':
    path = './kraken_image/' + str(hero) + '.png'
  else:
    path = './yeti_image/' + str(hero) + '.png'
  # Навести щоб робив скрол 
  pyautogui.click(START_POSITION_X + 380, START_POSITION_Y + 200)
  pyautogui.moveTo(START_POSITION_X + 300, START_POSITION_Y + 420)
  doScreenshot()
  result = cv2.matchTemplate(cv2.imread('screenshot.png'), cv2.imread(path), cv2.TM_CCOEFF_NORMED)
  (min_x, max_y, minloc, maxloc) = cv2.minMaxLoc(result) 
  if  max_y < 0.95: 
    pyautogui.scroll(-100)  
    time.sleep(1) 
    pickHero(type, hero)
  else:
      pyautogui.click(START_POSITION_X + maxloc[0] + 10, START_POSITION_Y + maxloc[1] + 10)
      time.sleep(0.5) 
      pyautogui.click(START_POSITION_X + 380, START_POSITION_Y + 815)
      print('Герой успішно обраний')    

# Переміщення до кракену
def moveToKraken():
  global START_POSITION_X, START_POSITION_Y
  pyautogui.moveTo(START_POSITION_X + 260, START_POSITION_Y + 825)
  pyautogui.mouseDown()
  pyautogui.moveTo(START_POSITION_X + 260 + 40, START_POSITION_Y + 825 - 70)
  time.sleep(1)
  pyautogui.mouseUp()
  # pyautogui.keyDown('w')
  # pyautogui.keyDown('d')
  # time.sleep(0.35)
  # pyautogui.keyUp('d')
  # time.sleep(0.15)
  # pyautogui.keyUp('w')
  print('Перемістився до кракену')

# Отримання нагороди
def closeTotal():
  checkLag()
  doScreenshot()
  result = cv2.matchTemplate(cv2.imread('screenshot.png'), cv2.imread('./image/total.png'), cv2.TM_CCOEFF_NORMED)
  (min_x, max_y, minloc, maxloc) = cv2.minMaxLoc(result)
  if  max_y < 0.98: 
    time.sleep(5) 
    closeTotal()
  else:
    print('Закриття результатів з винагородою', max_y)
    pyautogui.click(START_POSITION_X + maxloc[0] + 3, START_POSITION_Y + maxloc[1] + 3)
    time.sleep(1) 
    pyautogui.click(START_POSITION_X + maxloc[0] + 3, START_POSITION_Y + maxloc[1] + 3)

# Вибір для бонусних відсотків
def checkAndClose15():
  doScreenshot()
  result = cv2.matchTemplate(cv2.imread('screenshot.png'), cv2.imread('./image/pickHero.png'), cv2.TM_CCOEFF_NORMED)
  (min_x, max_y, minloc, maxloc) = cv2.minMaxLoc(result)
  if  max_y > 0.98:
    print('Закриття бонусу в 15%', max_y)
    pickHero('kraken', 2)

# Перевірка на бонуси каменів у відсотках
def checkAndPickBonus(path):
  doScreenshot()
  result = cv2.matchTemplate(cv2.imread('screenshot.png'), cv2.imread(path), cv2.TM_CCOEFF_NORMED)
  (min_x, max_y, minloc, maxloc) = cv2.minMaxLoc(result)
  if  max_y > 0.98:
    print('Прийняття бонусних каменів', max_y)
    pyautogui.click(START_POSITION_X + maxloc[0] + 150, START_POSITION_Y + maxloc[1] + 140)
    time.sleep(0.5)
    pyautogui.click(START_POSITION_X + maxloc[0] + 150, START_POSITION_Y + maxloc[1] + 140)
    time.sleep(0.5)
    pyautogui.click(START_POSITION_X + maxloc[0] + 150, START_POSITION_Y + maxloc[1] + 140)

# Завершення підземелля
def finishDangeon():
  checkLag()
  doScreenshot()
  result = cv2.matchTemplate(cv2.imread('screenshot.png'), cv2.imread('./image/exit.png'), cv2.TM_CCOEFF_NORMED)
  (min_x, max_y, minloc, maxloc) = cv2.minMaxLoc(result)
  print(max_y)
  if  max_y > 0.98:
    print('Завершення підземелля', max_y)
    pyautogui.click(START_POSITION_X + maxloc[0] + 20, START_POSITION_Y + maxloc[1] + 10)
    # time.sleep(10)
    # pyautogui.click(START_POSITION_X + 270, START_POSITION_Y + 270)
  else:
    time.sleep(1)
    finishDangeon()

# Пропуск фарму на кракені
def skipKrakenFarm():
  pyautogui.click(START_POSITION_X + 260, START_POSITION_Y + 130)
  time.sleep(0.5)
  pyautogui.click(START_POSITION_X + 350, START_POSITION_Y + 625)
  print('Прокачка на кракені пропущена')

# Перевірка на завантаження рівня йеті
def awaitLoadYetiLvl():
  checkLag()
  doScreenshot()
  result = cv2.matchTemplate(cv2.imread('screenshot.png'), cv2.imread('./yeti_image/game_pult.png'), cv2.TM_CCOEFF_NORMED)
  (min_x, max_y, minloc, maxloc) = cv2.minMaxLoc(result)
  if  max_y < 0.95:
     time.sleep(1)
     awaitLoadYetiLvl()
  else:   
    print('Рівень завантажено')
    time.sleep(1)

# Перевірка позиції та переміщення до боса
def moveToYeti():
  # Перевірими на якій ми позиції
  checkMyPosition()
  # Переміщення до босу
  moveHeroToArena()

def checkMyPosition():
  doScreenshot()
  result = cv2.matchTemplate(cv2.imread('screenshot.png'), cv2.imread('./yeti_image/desk.png'), cv2.TM_CCOEFF_NORMED)
  (min_x, max_y, minloc, maxloc) = cv2.minMaxLoc(result)
  print('Позиція вказівника', max_y, maxloc[0])
  if  max_y > 0.8:
    if maxloc[0] > 220:
      print('Потрібно нижче', START_POSITION_X, maxloc[0])
      moveDown()

def moveDown():
  global START_POSITION_X, START_POSITION_Y
  pyautogui.moveTo(START_POSITION_X + 260, START_POSITION_Y + 825)
  pyautogui.mouseDown()
  pyautogui.moveTo(START_POSITION_X + 320, START_POSITION_Y + 895)
  time.sleep(0.2)
  pyautogui.mouseUp()
  print('Перемістився нижче')


def moveHeroToArena():
  global START_POSITION_X, START_POSITION_Y
  pyautogui.moveTo(START_POSITION_X + 260, START_POSITION_Y + 825)
  pyautogui.mouseDown()
  pyautogui.moveTo(START_POSITION_X + 320, START_POSITION_Y + 755)
  time.sleep(2.3)
  pyautogui.mouseUp()
  print('Прийшов до йеті')  


def checkBlack():
  doScreenshot()
  result = cv2.matchTemplate(cv2.imread('screenshot.png'), cv2.imread('./image/black.png'), cv2.TM_CCOEFF_NORMED)
  (min_x, max_y, minloc, maxloc) = cv2.minMaxLoc(result)
  print('checkBlack', max_y)
  if  max_y > 0.98:
    print('OK')
    time.sleep(0.1)
    checkBlack()
  else: 
    print('New try')
    time.sleep(0.1)
    checkBlack()

def checkBlue():
  doScreenshot()
  result = cv2.matchTemplate(cv2.imread('screenshot.png'), cv2.imread('./image/blue.png'), cv2.TM_CCOEFF_NORMED)
  (min_x, max_y, minloc, maxloc) = cv2.minMaxLoc(result)
  print('checkBlue', max_y)
  if  max_y > 0.98:
    print('checkBlue OK')
  else: 
    print('checkBlue New try')
    time.sleep(1)
    checkBlue()

def checkDelBlack():
  doScreenshot()
  result = cv2.matchTemplate(cv2.imread('screenshot.png'), cv2.imread('./image/black.png'), cv2.TM_CCOEFF_NORMED)
  (min_x, max_y, minloc, maxloc) = cv2.minMaxLoc(result)
  print('checkBlack', max_y)
  if  max_y > 0.98:
    print('checkBlack exist')
    time.sleep(0.3)
    checkDelBlack()
  else: 
    print('checkBlack null')

   


# Функція для підбору кракенв в чаосі
def pickChaosKraken():
  # Жмем почати
  pressStartGame()
  # Чекаэмо завантаження
  awaitPickField()
  # Перевіряємо чи кракен
  check = checkKraken()
  if check == False:
    pickChaosKraken()
  else:
   print('Обираємо героя') 

# Клік на кнопку старт
def awaitPickField():
  global START_POSITION_X, START_POSITION_Y
  doScreenshot()
  result = cv2.matchTemplate(cv2.imread('screenshot.png'), cv2.imread('./chaos_image/pick_field.png'), cv2.TM_CCOEFF_NORMED)
  (min_x, max_y, minloc, maxloc) = cv2.minMaxLoc(result)
  print('Очікуємо завантаження', max_y)
  if  max_y > 0.9:
    print('Меню завантажено')
  else:
    time.sleep(1)
    awaitPickField()

# Перевіряємо чи кракен 
def checkKraken():
  global START_POSITION_X, START_POSITION_Y
  doScreenshot()
  result = cv2.matchTemplate(cv2.imread('screenshot.png'), cv2.imread('./chaos_image/kraken_lvl.png'), cv2.TM_CCOEFF_NORMED)
  (min_x, max_y, minloc, maxloc) = cv2.minMaxLoc(result)
  print('Перевірка чи кракен', max_y)
  if  max_y > 0.9:
    print('Кракен - можна обирати героя')
    return True
  else:
    print('Не кракен - перезапуск')
    pyautogui.click(START_POSITION_X + 240, START_POSITION_Y + 100)
    time.sleep(1)
    return False

# Очікування завантаження
def awaitLoadKrakenShip():
  global START_POSITION_X, START_POSITION_Y
  doScreenshot()
  result = cv2.matchTemplate(cv2.imread('screenshot.png'), cv2.imread('./chaos_image/load_lvl.png'), cv2.TM_CCOEFF_NORMED)
  (min_x, max_y, minloc, maxloc) = cv2.minMaxLoc(result)
  if  max_y > 0.9:
    print('Завантаження триває')
    time.sleep(0.3)
    awaitLoadKrakenShip()
  else:
    print('Завантаження завершено')

# Переміщення до кракену з пушкою
def moveToKraken2():
  global START_POSITION_X, START_POSITION_Y
  pyautogui.moveTo(START_POSITION_X + 260, START_POSITION_Y + 400)
  pyautogui.mouseDown()
  pyautogui.moveTo(START_POSITION_X + 260 - 30, START_POSITION_Y + 400 - 50)
  time.sleep(0.2)
  pyautogui.moveTo(START_POSITION_X + 260 + 50, START_POSITION_Y + 400 - 40)
  time.sleep(0.3)
  pyautogui.mouseUp()
  print('Перемістився до кракену')  

# Очікуємо фінішу
def awaitFinishChaos():
  checkLag()
  global START_POSITION_X, START_POSITION_Y
  doScreenshot()
  result = cv2.matchTemplate(cv2.imread('screenshot.png'), cv2.imread('./chaos_image/finish lvl.png'), cv2.TM_CCOEFF_NORMED)
  (min_x, max_y, minloc, maxloc) = cv2.minMaxLoc(result)
  if  max_y > 0.9:
    print('Кракен вбитий')
  else:
    time.sleep(3)
    awaitFinishChaos()

# Очікуємо фінішу
def finishChaos():
  global START_POSITION_X, START_POSITION_Y
  time.sleep(0.5)
  pyautogui.click(START_POSITION_X + 120, START_POSITION_Y + 430)
  time.sleep(0.5)
  pyautogui.click(START_POSITION_X + 380, START_POSITION_Y + 810)
  time.sleep(1)
  awaitLoadKrakenShip()
  time.sleep(0.5)
  pyautogui.click(START_POSITION_X + 30, START_POSITION_Y + 65)
  time.sleep(0.5)
  pyautogui.click(START_POSITION_X + 250, START_POSITION_Y + 730)


# Переміщення до кракену з пушкою
def moveToKraken3():
  global START_POSITION_X, START_POSITION_Y
  print('in move: ',START_POSITION_X, START_POSITION_Y)
  pyautogui.moveTo(START_POSITION_X + 260, START_POSITION_Y + 400)
  time.sleep(0.1)
  pyautogui.mouseDown()
  time.sleep(0.1)
  pyautogui.moveTo(START_POSITION_X + 260 - 30, START_POSITION_Y + 400 - 50)
  time.sleep(1.5)
  pyautogui.moveTo(START_POSITION_X + 260 + 50, START_POSITION_Y + 400 - 40)
  time.sleep(0.5)
  pyautogui.mouseUp()
  print('Перемістився до кракену')  