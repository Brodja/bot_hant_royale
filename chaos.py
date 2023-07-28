import methods
import time

# кубки - 2 338 715
# поверхи - 83
# кракен - 13589 - 9728 = 3861 - 117 р
# лаба - 5444 - 3594 = 1850
# час 17:30 - 18:33 = ? минут

def startChaosLogic(): 
    methods.lastUpdate = time.time()
    for roll in range(1, 10):
      totalRange = 15
      print('Запуск chaos')
       # Затримка для початку логіки
      time.sleep(1)
      #  Пошук положення емулятору
      methods.findPositionEmulator()
      # Запуск циклу проходжен
      for num in range(1, totalRange):
        methods.lastUpdate = time.time()
        timeStart = time.time()
        print('Початок основного циклу')
        # Підбір кракену
        methods.pickChaosKraken()
        # Вибір анубіса  
        methods.pickHero('kraken', 22) #17 13
        time.sleep(1)
        # Очікування завантаження
        methods.awaitLoadKrakenShip()
        # time.sleep(2)
        # Переміщення до босу
        # methods.moveToKraken2()
        methods.moveToKraken3()
        # Очікуємо фінішу
        methods.awaitFinishChaos()
        # Вибір герою для наступного рівня та його завершення
        time.sleep(1)
        methods.finishChaos()
        # Отримання нагороди
        methods.closeTotal()
        time.sleep(3)
        # Вибір для бонусних відсотків
        methods.checkAndClose15()
        time.sleep(1)
        # Завершення підземелля
        methods.finishDangeon()
        print('ВСЬОГО РІВЕНЬ -', round(time.time() - timeStart), 's | ', round((time.time() - timeStart) / 60, 2), 'm') 
        time.sleep(5)
      # Перезапуск гри
      methods.restartHuntRoyale()
