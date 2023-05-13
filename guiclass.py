#imports
from tkinter import *
from tkinter import ttk
from tkinter import filedialog as fd

from os.path import dirname, join

from misaclass import MisaClass

class MisaGUI:
    def __init__(self, root) -> None:
        #variable declaration
        self.absolute_path = dirname(__file__)
        self.bfr_filepath = join(self.absolute_path, "before")
        self.new_filepath = join(self.absolute_path, "after/sfx/default")

        # name of window
        root.title("MisaMix")
        # do not allow window resizing
        #root.resizable(False, False)
        # set window size
        root.geometry('300x150')

        mainframe = ttk.Frame(root, padding="3 3 12 12")
        mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
        root.columnconfigure(0, weight=1)
        root.rowconfigure(0, weight=1)

        #before folder labels and button
        self.bfr_text = StringVar(value=join(self.absolute_path, 
                                             "before"))

        self.bfr_label = ttk.Label(mainframe, textvariable=self.bfr_text)
        self.bfr_label.grid(column=1, row=1, sticky=(N, W))

        self.bfr_button = ttk.Button(mainframe, text="process folder",
                            command=self.openbfrdir)
        self.bfr_button.grid(column=2, row=1, sticky=(N, W))

        #new folder labels and button
        self.new_text = StringVar(value=join(self.absolute_path,
                                             "after\sfx\default"))

        self.new_label = ttk.Label(mainframe, textvariable=self.new_text)
        self.new_label.grid(column=1, row=2, sticky=(N, W))

        self.new_button = ttk.Button(mainframe, text="new",
                                    command=self.opennewdir)
        self.new_button.grid(column=2, row=2, sticky=(N, W))

        #run button
        self.run_button = ttk.Button(mainframe, text="run",
                                    command=self.main)
        self.new_button.grid(column=3, row=3, sticky=(E))

        for child in mainframe.winfo_children(): 
            child.grid_configure(padx=5, pady=5)
    
    def openbfrdir(self):
        self.bfr_filepath = fd.askdirectory(initialdir=self.absolute_path)
        self.bfr_text.set(self.bfr_filepath)

    def opennewdir(self):
        self.new_filepath = fd.askdirectory(initialdir=self.absolute_path)
        self.new_text.set(self.new_filepath)

    def main(self):
        self.misa = MisaClass(bfr_folder=self.bfr_filepath, new_folder=self.new_filepath)
        self.misa.main()

root = Tk()
MisaGUI(root)
root.mainloop()