from tkinter import *
import kraken
import yeti
import chaos
import methods
# РОЗМІР ЕМУЛЯТОРУ (самої гри) 520 * 920

root = Tk()
root['bg'] = '#fafafa'
root.title('Hunt bot')
root.wm_attributes('-alpha', 0.9)
root.geometry('250x250')
root.resizable(width=False, height=False)

# Функція для зупинення всіх процесів та їх завершенння
def stopAndClose():
    methods.running = False
    root.destroy()

# кнопки
btnKraken = Button(root, text='Kraken', bg='green',  width='20', height='3', command=kraken.startKrakenLogic)
btnYeti = Button(root, text='Yeti', bg='blue', width='20', height='3', command=yeti.startYetiLogic)
btnChaos = Button(root, text='Chaos', bg='yellow', width='20', height='3', command=chaos.startChaosLogic)
btnExit = Button(root, text='Exit', bg='red', width='20', height='3', command=stopAndClose)

btnYeti.pack()
btnKraken.pack()
btnChaos.pack()
btnExit.pack()

if __name__ == '__main__':
  root.mainloop()