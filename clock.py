from tkinter import *
from datetime import datetime
import pytz

root = Tk()
root.geometry("1200x600")
image_icon = PhotoImage(file="d:/ok/clock.png")
root.iconphoto(False, image_icon)

def times():
    home = pytz.timezone("Asia/Kolkata")
    local_time = datetime.now(home)
    current_time = local_time.strftime("%a %H:%M:%S")
    clock.config(text=current_time)
    name.config(text="India")

    home2 = pytz.timezone("America/New_York")
    local_time2 = datetime.now(home2)
    current_time2 = local_time2.strftime("%a %H:%M:%S")
    clock2.config(text=current_time2)
    name2.config(text="USA")

    home3 = pytz.timezone("Europe/London")
    local_time3 = datetime.now(home3)
    current_time3 = local_time3.strftime("%a %H:%M:%S")
    clock3.config(text=current_time3)
    name3.config(text="London")

    home4 = pytz.timezone("Asia/Tokyo")
    local_time4 = datetime.now(home4)
    current_time4 = local_time4.strftime("%a %H:%M:%S")
    clock4.config(text=current_time4)
    name4.config(text="Tokyo")

    home5 = pytz.timezone("Asia/Tokyo")

    clock.after(1000, times)

f = Frame(root, bd=5)
f.place(x=10, y=118, width=220, height=150)

name = Label(f, font=("Helvetica", 30, "bold"))
name.place(x=50, y=10)

logo = PhotoImage(file="d:/ok/ind.png")
image_label = Label(root, image=logo)
image_label.place(x=20, y=150)

clock = Label(f, font=("Helvetica", 20))
clock.place(x=5, y=80)

f2 = Frame(root, bd=5)
f2.place(x=300, y=118, width=220, height=150)

name2 = Label(f2, font=("Helvetica", 30, "bold"))
name2.place(x=30, y=10)

logo2 = PhotoImage(file="d:/ok/usa.png")
image_label2 = Label(root, image=logo2)
image_label2.place(x=290, y=150)

clock2 = Label(f2, font=("Helvetica", 20))
clock2.place(x=5, y=80)

f3 = Frame(root, bd=5)
f3.place(x=590, y=118, width=220, height=150)

name3 = Label(f3, font=("Helvetica", 30, "bold"))
name3.place(x=30, y=10)

logo3 = PhotoImage(file="d:/ok/eng.png")
image_label3 = Label(root, image=logo3)
image_label3.place(x=580, y=150)

clock3 = Label(f3, font=("Helvetica", 20))
clock3.place(x=5, y=80)

f4 = Frame(root, bd=5)
f4.place(x=880, y=118, width=220, height=150)

name4 = Label(f4, font=("Helvetica", 30, "bold"))
name4.place(x=30, y=10)

logo4 = PhotoImage(file="d:/ok/jap.png")
image_label4 = Label(root, image=logo4)
image_label4.place(x=870, y=150)

clock4 = Label(f4, font=("Helvetica", 20))
clock4.place(x=5, y=80)

times()
root.mainloop()
