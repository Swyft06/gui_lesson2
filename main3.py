from tkinter import *
from tkinter.ttk import *

root = Tk()
root.geometry("400x350")
root.title("Spin Box")

s = Spinbox(root,from_=0, to=100)
s.pack()



root.mainloop()
