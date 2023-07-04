from tkinter import *
import kraken
import yeti
from multiprocessing import Process, freeze_support
# РОЗМІР ЕМУЛЯТОРУ (самої гри) 520 * 920

root = Tk()
root['bg'] = '#fafafa'
root.title('Hunt bot')
root.wm_attributes('-alpha', 0.9)
root.geometry('250x200')
root.resizable(width=False, height=False)

freeze_support()
# Логіка кракену
# proc_kraken = Process(target=kraken.startKrakenLogic)
# Лоігка йеті
# proc_yeti = Process(target=yeti.start_run)

# Функція для зупинення всіх процесів та їх завершенння
def stopAndClose():
    print('Вхід у функцію зупинки')
    # global proc_kraken, proc_yeti
    # if proc_kraken.is_alive():
    #   print('Зупинення кракену')
    #   proc_kraken.terminate()
    #   proc_kraken.kill()
    # if proc_yeti.is_alive():  
    #   print('Йеті кракену')
    #   proc_yeti.terminate()
    #   proc_yeti.kill()
    root.destroy()

# кнопки
# btnKraken = Button(root, text='Kraken', bg='green',  width='20', height='3', command=proc_kraken.start)
btnKraken = Button(root, text='Kraken', bg='green',  width='20', height='3', command=kraken.startKrakenLogic)
# btnYeti = Button(root, text='Yeti', bg='blue', width='20', height='3', command=proc_yeti.start)
btnYeti = Button(root, text='Yeti', bg='blue', width='20', height='3', command=yeti.start_run)
btnExit = Button(root, text='Exit', bg='red', width='20', height='3', command=stopAndClose)

btnYeti.pack()
btnKraken.pack()
btnExit.pack()

if __name__ == '__main__':
  root.mainloop()