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
        root.resizable(False, False)
        #root.geometry("550x150")
        

        

        #mainframe to prevent widget off colour
        mainframe = ttk.Frame(root, padding="3 3 12 12")
        mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
        root.columnconfigure(0, weight=1)
        root.rowconfigure(0, weight=1)

        #before folder labels and button
        self.descbfr_lbl = ttk.Label(mainframe, text="Input:")
        self.descbfr_lbl.grid(column=0, row=0, sticky=(N, W))
        
        self.bfr_text = StringVar(value=self.bfr_filepath)

        self.bfr_lbl = ttk.Label(mainframe, textvariable=self.bfr_text, width=60)
        self.bfr_lbl.grid(column=1, row=0, sticky=(N, W))

        self.bfr_button = ttk.Button(mainframe, text="Open",
                                        command=self.openbfrdir)
        self.bfr_button.grid(column=2, row=0, sticky=(N, W))
        

        #new folder labels and button
        self.descnew_lbl = ttk.Label(mainframe, text="Output:")
        self.descnew_lbl.grid(column=0, row=1, sticky=(N, W))

        self.new_text = StringVar(value=self.new_filepath)

        self.new_lbl = ttk.Label(mainframe, textvariable=self.new_text, width=60)
        self.new_lbl.grid(column=1, row=1, sticky=(N, W))

        self.new_button = ttk.Button(mainframe, text="Open",
                                    command=self.opennewdir)
        self.new_button.grid(column=2, row=1, sticky=(N, W))

        #success label
        self.success_text = StringVar()
        self.success_lbl = ttk.Label(mainframe, textvariable=self.success_text)
        self.success_lbl.grid(column=1, row=3, sticky=S)
        

        #run button
        self.run_button = ttk.Button(mainframe, text="Run", command=self.main)
        self.run_button.grid(column=3, row=3, sticky=(E))

        for child in mainframe.winfo_children(): 
            child.grid_configure(padx=5, pady=5)
    
    def openbfrdir(self):
        bfr_filepath = fd.askdirectory(initialdir=self.absolute_path)
        if bfr_filepath == "":
            pass
        else:
            self.bfr_filepath = bfr_filepath
            self.bfr_text.set(self.bfr_filepath)

    def opennewdir(self):
        new_filepath = fd.askdirectory(initialdir=self.absolute_path)
        if new_filepath == "":
            pass
        else:
            self.new_filepath = new_filepath
            self.new_text.set(self.new_filepath)

    def main(self):
        self.misa = MisaClass(bfr_folder=self.bfr_filepath, new_folder=self.new_filepath)
        if self.misa.main():
            self.success_text.set("soundpack converted successfully")
            self.success_lbl.config(foreground='green')
            root.bell()
        else:
            self.success_text.set("soundpack failed to be converted")
            self.success_lbl.config(foreground='red')
            root.bell()


root = Tk()
MisaGUI(root)
root.mainloop()