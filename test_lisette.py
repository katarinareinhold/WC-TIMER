from tkinter import *
from tkinter import ttk

raam = Tk()
raam.title("kast")
raam.geometry("300x160")

tekstisilt = ttk.Label(raam, text="Lisette")
tekstisilt.place(x=120, y=80)

raam.mainloop()