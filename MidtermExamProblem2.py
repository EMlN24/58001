from tkinter import *
class MyWindow:
        def __init__(self, win):
                self.lbl_title = Label(win, text="My Full Name")
                self.lbl_title.place(x=200, y=40)

                self.lbl_firstname = Label(win, text="Enter Given Name:")
                self.lbl_firstname.place(x=100, y=80)

                self.lbl_middlename = Label(win, text="Enter Middle Name:")
                self.lbl_middlename.place(x=100, y=110)

                self.lbl_lastname = Label(win, text="Enter Last Name:")
                self.lbl_lastname.place(x=100, y=140)

                self.lbl_fullname = Label(win, text="My Full Name is:")
                self.lbl_fullname.place(x=100, y=180)

                self.txt_firstname = Entry(win, bd=2)
                self.txt_firstname.place(x=275, y=80)

                self.txt_middlename = Entry(win, bd=2)
                self.txt_middlename.place(x=275, y=110)

                self.txt_lastname = Entry(win, bd=2)
                self.txt_lastname.place(x=275, y=140)

                self.txt_fullname = Entry(win, bd=2, width=30)
                self.txt_fullname.place(x=275, y=180)

                self.btn_dsplyflnm = Button(win, text="Show Full Name")
                self.btn_dsplyflnm.place(x=200, y=210)
                self.btn_dsplyflnm.bind('<Button-1>', self.display)

        def display(self, display):
                 self.txt_fullname.delete(0, 'end')
                 firstname = str(self.txt_firstname.get())
                 middlename = str(self.txt_middlename.get())
                 lastname = str(self.txt_lastname.get())
                 fullname = firstname + " " + middlename + " " + lastname + " "
                 self.txt_fullname.insert(END, str(fullname))

window = Tk()
mywin = MyWindow(window)
window.geometry("500x300+10+10")
window.title("Midterm Exam Problem 2")
window.mainloop()