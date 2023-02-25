import methods
import time
# 260 130 && 350 625

def run(count):  
  time.sleep(3)
  methods.findStartPosition()
  print('START_POSITION_X 2', methods.START_POSITION_X)
  for num in range(1,count):
    methods.pressStartGame()
    time.sleep(1)
    methods.checkReloadGems()
    methods.awaitGameArena('./kraken_image/game_pult.png')
    methods.disconnect()
    time.sleep(1)
    methods.skipKrakenFarm()
    time.sleep(1)
    methods.awaitGameArena('./kraken_image/game_pult.png')
    methods.checkKillBoss()
    for hero in range(2,21):
      methods.pickHero('./kraken_image/' + str(hero) + '.png', hero)
      methods.awaitGameArena('./kraken_image/game_pult.png')
      methods.skipKrakenFarm()
      if hero in [2, 4, 10, 17, 20]:
         time.sleep(1)
         methods.awaitGameArena('./kraken_image/game_pult.png')
         methods.moveToKraken()
      if hero < 20:
        methods.checkKillBoss()
      else:
        print('Finish')
    methods.closeTotal()
    time.sleep(1)
    methods.checkAndClose15()
    time.sleep(1)
    methods.checkAndPickBonus()
    time.sleep(1)
    methods.exitGame()


if __name__=="__main__":
    run(3) 