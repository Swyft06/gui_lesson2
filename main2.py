from tkinter import *
from tkinter.ttk import *
import time

root = Tk()

progressbar = Progressbar(root, orient = HORIZONTAL, length = 100,mode = "indeterminate")
progressbar.pack(pady=10)

def Bar():
    progressbar['value'] = 20
    root.update_idletasks()
    time.sleep(1)

    progressbar['value'] = 40
    root.update_idletasks()
    time.sleep(1)

    progressbar['value'] = 60
    root.update_idletasks()
    time.sleep(1)

    progressbar['value'] = 80
    root.update_idletasks()
    time.sleep(1)

    progressbar['value'] = 100
    root.update_idletasks()
    time.sleep(1)






btn1 = Button(root, text = 'Start', command = Bar)
btn1.pack(pady=15)

root.mainloop()
