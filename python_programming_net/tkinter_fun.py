# Exercise 38
# Tkinter

from tkinter import *


class Window(Frame):

    # Parent Widget, initialized per the tk documentation
    def __init__(self, master=None):
        # __init__ is called when ever an object of the class is constructed
        Frame.__init__(self, master)

        # Our Master widget or main frame
        self.master = master


# root Window
root = Tk()


app = Window(root)
# Generates our main window
root.mainloop()
