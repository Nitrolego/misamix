#imports for gui
from tkinter import *
from tkinter import ttk
from tkinter import filedialog as fd

#import script

#import misamix
#importing script runs it. not intended behaviour

# def runthisscript(*args):
#     exec(misamix)
def runfile():
    fd.askopenfilename()
    #this allows show open file dialog. has options


root = Tk()
#title of window
root.title("i'm trying this out")
# do not allow file resizing
root.resizable(False, False)
# set window size
root.geometry('300x150')



#adding mainframe
mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

ttk.Button(mainframe, text="clickme", command=runfile).grid(column=2, row=2, sticky=N)

root.mainloop()