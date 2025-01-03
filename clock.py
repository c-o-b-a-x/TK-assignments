from tkinter import Tk, Label
from time import strftime


root = Tk()
root.title("Clock")


time_label = Label(root, font=("Arial", 50), fg="green", bg="black")
time_label.pack(pady=10)

day_label = Label(root, font=("Arial", 30), fg="white", bg="black")
day_label.pack(pady=5)

date_label = Label(root, font=("Arial", 30), fg="white", bg="black")
date_label.pack(pady=5)


def update_clock():
    current_time = strftime('%I:%M:%S %p') 
    time_label.config(text=current_time)

    current_day = strftime('%A')  
    day_label.config(text=current_day)

    current_date = strftime('%B %d, %Y')  
    date_label.config(text=current_date)

    root.after(1000, update_clock)

update_clock()


root.mainloop()