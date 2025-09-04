import tkinter as tk

raam = tk.Tk()
raam.title("Minu nimi on...")
raam.geometry("400x200")

silt = tk.Label(raam, text="Katarina Reinhold")
silt.place(x=120, y=80)

raam.mainloop()
