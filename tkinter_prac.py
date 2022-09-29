"""
    This is just for Tkinter practice 

"""

from tkinter import *
 
root = Tk()
 

root.title("Tkinter Practice")

root.geometry('300x200')
 
lbl = Label(root, text = "Press me!")
lbl.grid()
 
def clicked():
    lbl.configure(text = "The button has been pressed")
 
btn = Button(root, text = "BUTTON" ,
             fg = "red", command=clicked)
# set Button grid
btn.grid(column=1, row=0)
 

root.mainloop()