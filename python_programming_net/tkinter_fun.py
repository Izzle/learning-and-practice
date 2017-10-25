# Exercise 38, 39, 40
# Tkinter

from tkinter import *


class Window(Frame):

    # Parent Widget, initialized per the tk documentation
    def __init__(self, master=None):
        # __init__ is called when ever an object of the class is constructed
        Frame.__init__(self, master)
        # Our Master widget or main frame
        self.master = master
        # Not from Tk library. We're creating this function below.
        self.init_window()

    # initialize our window
    def init_window(self):

        self.master.title("GUI")
        # Says: We are filling up the windows. Adjust dimensions as needed.
        self.pack(fill=BOTH, expand=1)
        # Button() is function within tkinter. We set text and gave it a cmd.
        # command=self.cleint_exit is a basic event handler that exits the app.
        quitButton = Button(self, text='Quit', command=self.client_exit)

        quitButton.place(x=0, y=0)

    def client_exit(self):
        exit()


# root Window
root = Tk()
# Dimensions of our window
root.geometry("600x450")


app = Window(root)
# Generates our main window
root.mainloop()
