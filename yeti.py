import methods
import time
# 260 130 && 350 625

# Алгоритм для йеті

def startYetiLogic():  
  totalRange = 20
  # Затримка для початку логіки
  time.sleep(3)
  #  Пошук положення емулятору
  methods.findPositionEmulator()
  # Запуск циклу проходжень
  for num in range(1, totalRange):
    print('Початок основного циклу')
    # Клік на кнопку старт
    methods.pressStartGame()
    time.sleep(1)
    # Перевірка на пропозицію токенів
    methods.checkReloadGems()
    # Перевірка на знаходження напарника та розрив зв'язку. 
    methods.awaitFindUserAndDisconnect()
    # Перевірка на завантаження рівня йеті
    methods.awaitLoadYetiLvl()
    # Переміщення до боса
    methods.moveToYeti()
    # Очікування смерті боса
    methods.checkKillBoss()
    # Починається цикл вибору героїв
    for hero in range(2,21):
      methods.pickHero('yeti', hero)
      methods.awaitLoadYetiLvl()
      # Переміщення до боса
      methods.moveToYeti()
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
    methods.checkAndPickBonus('./yeti_image/get_bonus.png')
    time.sleep(1)
    # Завершення підземелля
    methods.finishDangeon()
    time.sleep(5)
   
