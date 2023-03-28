from tkinter import *

window = Tk()
window.geometry("500x400+10+10")
window.title("My first GUI")

btn1 = Button(text="Click Me", bg="gold", fg="black")
btn1.place(x=220, y=190)

txtfld = Entry(window, border=10)
txtfld.place(x=185, y=100)

lbl = Label(window, text="My first Demo", font="Verdana")
lbl.place(x=200, y=45)

window.mainloop()
