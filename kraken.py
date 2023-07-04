import methods
import time
# 260 130 && 350 625

# Алгоритм для кракену

def startKrakenLogic():  
  totalRange = 2
  print('Запуск кракена')
  # Затримка для початку логіки
  time.sleep(3)
  #  Пошук положення емулятору
  methods.findPositionEmulator()
  # Запуск циклу проходжень
  for count in range(1, totalRange):
    print('Початок основного циклу')
    # Клік на кнопку старт
    methods.pressStartGame()
    time.sleep(1)
    # Перевірка на пропозицію токенів
    methods.checkReloadGems()
    # Перевірка на знаходження напарника та розрив зв'язку. 
    methods.awaitFindUserAndDisconnect()
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
      methods.pickHero('kraken', hero)
      # Перевірка на завантаження рівня
      methods.awaitLoadKrakenLvl()
      # Пропуск фарму на кракені
      methods.skipKrakenFarm()
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
    time.sleep(5)
