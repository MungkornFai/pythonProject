import tkinter as tk
from tkinter import *
from tkinter import ttk


class Exchange:
    def __init__(self, root):
        self.root = root
        self.root.title("Exchange")
        self.root.geometry("500x400")

        MainFrame = Frame(self.root, bg="#15cddb", width=500, height=400, bd=10)
        MainFrame.grid()

        labelTitle = Label(MainFrame, bg="#15cddb", fg="blue", font=15, text="Exchange Program").place(x=155, y=50)

        cbObtion =ttk.Combobox(MainFrame, text="Choose Options",)
        cbObtion['values'] = ("ktob", "btok")
        cbObtion.place(x=50, y=50)
        cbObtion.current(0)

        txkInput = Entry(MainFrame, font=10, textvariable="")
        txkInput.place(x=200, y=50)

        inputBox = Label(MainFrame, text="Enter money", bg="#15cddb")
        inputBox.place(x=50, y=100)

        inputBox = Entry(MainFrame, font=10, textvariable="")
        inputBox.place(x=200, y=100)

        inputBox = Label(MainFrame, text="Enter rate", bg="#15cddb")
        inputBox.place(x=50, y=150)

        txkInput = Entry(MainFrame, font=10, textvariable="")
        txkInput.place(x=200, y=150)






if __name__ == "__main__":
    root = Tk()
    application = Exchange(root)
    root.mainloop()
