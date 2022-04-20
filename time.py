from tkinter import *
from time import *

def update():
    time_string = strftime("%I:%M:%S %p")
    time.config(text=time_string)

    day_string = strftime("%A")
    day.config(text=day_string)

    date_string = strftime("%B %d, %Y")
    date.config(text=date_string)

    window.after(1000, update)


window = Tk()
window.title("Clock")

time = Label(window, font=("Segoe UI", 40), fg="#00FF00", bg="black")
time.pack()

day = Label(window, font=("Segoe UI", 20), fg="black")
day.pack()

date = Label(window, font=("Segoe UI", 20), fg="black")
date.pack()

update()

window.mainloop()