#imports
from tkinter import *
from tkinter import ttk
from tkinter import filedialog as fd

from babel.support import Translations

from os.path import dirname, join

from misaclass import MisaClass

class MisaGUI(Frame):
    def __init__(self, language, master=None) -> None:
        Frame.__init__(self, master)

        LOCALE_PATH = "locale"

        translations = Translations.load(LOCALE_PATH, [language])
        _ = translations.gettext

        # name of window
        self.master.title("MisaMix")
        # do not allow window resizing
        self.master.resizable(False, False)

        #mainframe to prevent widgets being the wrong colour
        mainframe = ttk.Frame(self, padding="3 3 12 12")

        #variable declaration
        self.absolute_path = dirname(__file__)
        self.bfr_filepath = join(self.absolute_path, "before")
        self.new_filepath = join(self.absolute_path, "after/sfx/default")
        self.bfr_text = StringVar(value=self.bfr_filepath)
        self.new_text = StringVar(value=self.new_filepath)
        self.select_text = StringVar(value=_("Select your input and output directories"))
        self.success_text = StringVar(value=_("Soundpack converted successfully!"))
        self.fail_text = StringVar(value=_("Soundpack failed to be converted."))
        self.en = BooleanVar(value=True)
        self.cn = BooleanVar()
        self.pl = BooleanVar()

        #menubar settings
        menubar = Menu(self)
        filemenu = Menu(menubar, tearoff=0)
        filemenu.add_radiobutton(label="English", 
                                 value=1,  
                                 variable=self.en, 
                                 command=self.changeeng)
        filemenu.add_radiobutton(label="简体中文 (Chinese Simplified)", 
                                 value=1,  
                                 variable=self.cn, 
                                 command=self.changecn)
        filemenu.add_radiobutton(label="Polski (Polish)", 
                                 value=1,  
                                 variable=self.pl, 
                                 command=self.changepl)
        #filemenu.add_command(label="Español (Spanish)", command=self.changees)
        filemenu.add_separator()
        menubar.add_cascade(label=_("Languages"), menu=filemenu)
        self.master.config(menu=menubar)

        #label declaration
        self.descbfr_lbl = ttk.Label(mainframe, text=_("Input:"))
        self.descnew_lbl = ttk.Label(mainframe, text=_("Output:"))
        self.bfr_lbl = ttk.Label(mainframe, textvariable=self.bfr_text, width=60)
        self.new_lbl = ttk.Label(mainframe, textvariable=self.new_text, width=60)
        self.success_lbl = ttk.Label(mainframe, textvariable=self.select_text)

        #button declaration
        self.bfr_btn = ttk.Button(mainframe, text=_("Browse"), command=self.openbfrdir)
        self.new_btn = ttk.Button(mainframe, text=_("Browse"), command=self.opennewdir)
        self.run_btn = ttk.Button(mainframe, text=_("Run"), command=self.main)

        #grid positioning of widgets
        self.grid()
        mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
        self.descbfr_lbl.grid(column=0, row=0, sticky=(N, W))
        self.bfr_lbl.grid(column=1, row=0, sticky=(N, W))
        self.bfr_btn.grid(column=2, row=0, sticky=(N, W))        
        self.descnew_lbl.grid(column=0, row=1, sticky=(N, W))
        self.new_lbl.grid(column=1, row=1, sticky=(N, W))
        self.new_btn.grid(column=2, row=1, sticky=(N, W))
        self.success_lbl.grid(column=1, row=3, sticky=S)
        self.run_btn.grid(column=2, row=3, sticky=(E))

        for child in mainframe.winfo_children(): 
            child.grid_configure(padx=5, pady=5)

    def changecn(self):
        self.destroy()
        self.__init__("zh_Hans")
        self.en.set(False)
        self.cn.set(True)

    def changeeng(self):
        self.destroy()
        self.__init__("en_MY")
        self.en.set(True)

    def changepl(self):
        self.destroy()
        self.__init__("pl_PL")
        self.en.set(False)
        self.pl.set(True)

    def changees(self):
        self.destroy()
        self.__init__("es_MX")

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
        misa = MisaClass(bfr_folder=self.bfr_filepath, new_folder=self.new_filepath)
        if misa.main():
            self.success_lbl.config(textvariable=self.success_text)
            self.success_lbl.config(foreground='green')
            self.master.bell()
        else:
            self.success_lbl.config(textvariable=self.fail_text)
            self.success_lbl.config(foreground='red')
            self.master.bell()