from time import *
from tkinter import *
import tkinter as tk
from tkinter.messagebox import showinfo


def update():
    time_string = strftime("%I:%M:%S %p")
    time_label.config(text=time_string)

    day_string = strftime("%A")
    day_label.config(text=day_string)

    date_string = strftime("%B %d, %Y")
    date_label.config(text=date_string)

    window.after(1000, update)


def About():
    showinfo("About this program", "This is a program written by DevCodex....")


window = Tk()
window.title("Clock")
window.resizable(False, False)
p1 = PhotoImage(False, file="clock.png")
window.iconphoto(False, p1)

time_label = Label(window, font=("Ink Free", 50), fg="#00FF00", bg="black")
time_label.pack()

day_label = Label(window, font=("Ink Free", 25))
day_label.pack()

date_label = Label(window, font=("Ink Free", 30))
date_label.pack()

menu_bar = Menu(window)
window.config(menu=menu_bar)
help_menu = Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Help", command=About)

update()

window.mainloop()
