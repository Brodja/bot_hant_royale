import methods
import time
# 260 130 && 350 625

# Алгоритм для кракену

def startKrakenLogic():  
  for roll in range(1, 10):
    methods.lastUpdate = time.time()
    totalRange = 3
    timeStart = time.time()
    print('Запуск кракена')
    # Затримка для початку логіки
    time.sleep(3)
    #  Пошук положення емулятору
    methods.findPositionEmulator()
    # Запуск циклу проходжень
    for count in range(1, totalRange):
      print('Початок основного циклу', count)
      # Клік на кнопку старт
      methods.pressStartGame()
      time.sleep(1)
      # Перевірка на пропозицію токенів
      methods.checkReloadGems()
      # Перевірка на знаходження напарника та розрив зв'язку. 
      methods.awaitFindUserAndDisconnect()
      time.sleep(10)
      # Перевірка на завантаження рівня
      methods.awaitLoadKrakenLvl()
      # Пропуск фарму на кракені
      methods.skipKrakenFarm()
      # Очікування повного завантаження боса
      methods.awaitKrakenShip()
      # Вбивство боса
      # Очікування смерті боса
      methods.checkKillBoss()
      # Починається цикл вибору героїв
      for hero in range(2,21):
        methods.lastUpdate = time.time()
        methods.pickHero('kraken', hero)
        # Перевірка на завантаження рівня
        methods.awaitLoadKrakenLvl()
        # Пропуск фарму на кракені
        methods.skipKrakenFarm()
        time.sleep(1)
        # Очікування повного завантаження боса
        methods.awaitKrakenShip()
        # Перевірка чи треба герою бігти до кракена
        if hero in [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21]:
          methods.moveToKraken() 
        # Перевірка на останній рівень
        if hero < 20:
          methods.checkKillBoss()
        else:
          print('Останній рівень пройдено')
      # Отримання нагороди
      methods.closeTotal()
      time.sleep(1)
      # Вибір для бонусних відсотків
      methods.checkAndClose15()
      time.sleep(1)
      # Перевірка на бонуси каменів у відсотках
      methods.checkAndPickBonus('./kraken_image/get_bonus.png')
      time.sleep(1)
      # Завершення підземелля
      methods.finishDangeon()
      print('ВСЬОГО РІВЕНЬ -',round(time.time() - timeStart), 's | ', round((time.time() - timeStart) / 60, 2), 'm') 
      time.sleep(5)
    # Перезапуск гри
    methods.restartHuntRoyale()
