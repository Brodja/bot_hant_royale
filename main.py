from tkinter import *
import kraken
import yeti
from multiprocessing import Process, freeze_support

root = Tk()
root['bg'] = '#fafafa'
root.title('Hunt bot')
root.wm_attributes('-alpha', 0.9)
root.geometry('250x200')
root.resizable(width=False, height=False)

freeze_support()
proc_kraken = Process(target=kraken.start_run)
proc_yeti = Process(target=yeti.start_run)

def stopAndClose():
    global proc_kraken, proc_yeti
    if proc_kraken.is_alive():
      proc_kraken.terminate()
      proc_kraken.kill()
    if proc_yeti.is_alive():  
      proc_yeti.terminate()
      proc_yeti.kill()
    root.destroy()

btnKraken = Button(root, text='Kraken', bg='green',  width='20', height='3', command=proc_kraken.start)
btnKraken.pack()

btnYeti = Button(root, text='Yeti', bg='blue', width='20', height='3', command=proc_yeti.start)
btnYeti.pack()

btnExit = Button(root, text='Exit', bg='red', width='20', height='3', command=stopAndClose)
btnExit.pack()

if __name__ == '__main__':
  root.mainloop()