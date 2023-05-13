#imports
from tkinter import *
from tkinter import ttk
from tkinter import filedialog as fd

from misaclass import MisaClass

class MisaGUI:
    def __init__(self, root, misalogic) -> None:
        # name of window
        root.title("MisaMix")
        # do not allow window resizing
        root.resizable(False, False)
        # set window size
        root.geometry('300x150')

        self.onebutton = ttk.Button(text="clickme", 
                                    command=misalogic.main)
        self.onebutton.place(relx=0.5, rely=0.5, anchor=CENTER)

    def runfile(self):
        fd.askopenfilename()

root = Tk()
misa = MisaClass()
MisaGUI(root, misa)
root.mainloop()