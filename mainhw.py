from tkinter import *
from tkinter.ttk import *
import time
root = Tk()
root.geometry("500x500")
root.title("Gui")
root.config(background = "blue")

email_label = Label(root,text="Email")
email_label.place(x=40,y=60)
email_entry = Entry(root,width=50)
email_entry.place(x=100,y=60)
password_label=Label(root,text="Password")
password_label.place(x=20,y=100)
password_entry = Entry(root,width=50)
password_entry.place(x=100,y=100)

food_label = Label(root,text="What food would you like: Cheeseburger,pizza,fried chicken or none?")
food_label.place(x=10,y=150)
food_entry = Entry(root,width=30)
food_entry.place(x=10,y=180)
food_spinbox = Spinbox(root,from_=0, to=100)
food_spinbox.place(x=300,y=180)

drink_label = Label(root,text="What beverage would you like: Water,cola,lemonade or none?")
drink_label.place(x=10,y=250)
drink_entry = Entry(root,width=30)
drink_entry.place(x=10,y=280)
drink_spinbox = Spinbox(root,from_=0, to=100)
drink_spinbox.place(x=300,y=280)

dessert_label = Label(root,text="What dessert would you like: Ice cream,cake,cookies or none?")
dessert_label.place(x=10,y=350)
dessert_entry = Entry(root,width=30)
dessert_entry.place(x=10,y=380)
dessert_spinbox = Spinbox(root,from_=0, to=100)
dessert_spinbox.place(x=300,y=380)

progressbar = Progressbar(root, orient = HORIZONTAL, length = 100,mode = "determinate")
progressbar.place(x=200,y=460)

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

submit = Button(root, text = 'Submit Order', command = Bar)
submit.place(x=200,y=430)


root.mainloop()
