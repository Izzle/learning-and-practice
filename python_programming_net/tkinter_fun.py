# Exercise 38, 39, 40, 41, 42
# Tkinter basics: windows, buttons, event handling, menus,
# and images and text
#
# I know that my 'obvious' inline comments violate strict PEP8,
# but I'm learning and its easier for me to follow myself in this case.
# I'm sure Guido would approve.
#

from tkinter import *
from PIL import Image, ImageTk


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
        # quitButton = Button(self, text='Quit', command=self.client_exit)
        # quitButton.place(x=0, y=0)

        # Defining the menu. Menu() is a tkinter method
        menu_bar = Menu(self.master)
        self.master.config(menu=menu_bar)

        # Creating a basic menu with few functioning buttons
        file = Menu(menu_bar) # Creating a 'File' button for our dropdown menu
        file.add_command(label='Open', command=self.hello) # Non-functional 'Open' button
        file.add_command(label='Save', command=self.hello) # Non-functional 'Save' button
        file.add_separator() # Adds a space between the next menu item
        file.add_command(label='Exit', command=self.client_exit) # Adds the 'Exit' button to our File button / dropdown menu
        menu_bar.add_cascade(label='File', menu=file) # Adding 'FIle' to our menu. Think of cascade as the menu animation.

        edit = Menu(menu_bar) # Creates an 'Edit' button for our dropdown menu
        edit.add_command(label='Show Image', command=self.showImg)
        edit.add_command(label='Show Text', command=self.showTxt)
        menu_bar.add_cascade(label='Edit', menu=edit)

        helpmenu = Menu(menu_bar)
        helpmenu.add_command(label='About', command=self.hello)
        helpmenu.add_command(label='GUI Help', command=self.hello)
        menu_bar.add_cascade(label='Help', menu=helpmenu)

        edit.add_command()

    def client_exit(self):
        exit()

    def hello(self):
        print('Hello World!')


# root Window
root = Tk()
# Dimensions of our window
root.geometry("600x450")


app = Window(root)
# Generates our main window
root.mainloop()
