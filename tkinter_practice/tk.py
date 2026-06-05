from tkinter import *
from tkinter import ttk


myFrame = Tk()
myFrame.title="My Application"
myFrame.geometry("800x400")

# myBtn = Button(myFrame, text="Click")
# myBtn.pack(pady = 10, padx=10, side='left', anchor='nw')

# myInput = Entry(myFrame, width= 50)
# myInput.pack(pady = 10, padx=10, side='left', anchor='nw', ipady=4, fill='x', expand=True)


# button1 = Button(myFrame, text="button1")
# button1.grid(column=0, row=0, padx=10, pady=10, ipadx= 10, ipady=5)
# button2 = Button(myFrame, text="button2")
# button2.grid(column=1, row=0, padx=10, pady=10, ipadx= 10, ipady=5)

# button3 = Button(myFrame, text="button3")
# button3.grid(column=0, row=1, padx=10, pady=10, ipadx= 10, ipady=5)

# button4 = Button(myFrame, text="button4")
# button4.grid(column=1, row=1, padx=10, pady=10, ipadx= 10, ipady=5)

# button5 = Button(myFrame, text="button5")
# button5.grid(column=0, row=2, padx=10, pady=10, ipadx= 10, ipady=5, columnspan=2, sticky='we')

button6 = ttk.Button(myFrame, text="button6").pack()




  
myFrame.mainloop()