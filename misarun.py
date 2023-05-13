from misaclass import MisaClass
from guiclass import MisaGUI

#imports for gui
from tkinter import *
from tkinter import ttk

misa = MisaClass()

root = Tk()
MisaGUI(root)
root.mainloop()