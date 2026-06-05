from tkinter import *
from tkinter import ttk


registerApp = Tk()
registerApp.title("Age calculator")
registerApp.geometry("500x500")

titleApp = Label(registerApp, text="Age calculator", font="Calibre 20 bold")
titleApp.grid(row=0, column=2, pady=10, sticky="ew")
registerApp.grid_columnconfigure(0, weight=1)


fNameLabel = Label(registerApp, text="First name:", font="Calibre 16 ")
fNameLabel.grid(row=1, column=0, padx=10)

fNameEntry = Entry(registerApp, width=20)
fNameEntry.grid(row=1, column=1, sticky="w")




registerApp.mainloop()