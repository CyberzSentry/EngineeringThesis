from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from tkinter import filedialog
from threading import Thread
from .core import Core
import traceback


def displayMessage(title, message):
        messagebox.showinfo(title, message)

class Program:

    def __init__(self):

        #init main window
        self.window = Tk()
        self.window.title("Sensitive data finder")
        self.window.geometry('620x900')
        #init main tabs
        self.tabs = ttk.Notebook(self.window)
        self.tabSettings = ttk.Frame(self.tabs)
        self.tabResults = ttk.Frame(self.tabs)
        self.tabs.add(self.tabSettings, text="Settings")
        self.tabs.add(self.tabResults, text="Results")
        
        #init settings tab
        self.inPathLabel = Label(self.tabSettings, text='Input path:' )
        self.inPathLabel.grid(row = 0, column=0, padx=10, pady=10)
        self.inPath = Entry(self.tabSettings)
        self.inPath.grid(row=0, column=1, columnspan=4, padx=10, pady=10, sticky='we')
        self.inPathButton = Button(self.tabSettings, text="Browse", command=self.inBrowseButton)
        self.inPathButton.grid(row=0, column=5, padx=10, pady=10)
        
        self.outPathLabel = Label(self.tabSettings, text='Output path:' )
        self.outPathLabel.grid(row = 1, column=0, padx=10, pady=10)
        self.outPath = Entry(self.tabSettings)
        self.outPath.grid(row=1, column=1, columnspan=4, padx=10, pady=10, sticky='we')
        self.outPathButton = Button(self.tabSettings, text="Browse", command=self.outBrowseButton)
        self.outPathButton.grid(row=1, column=5, padx=10, pady=10)
        
        self.dictPathLabel = Label(self.tabSettings, text='Dictionary path:' )
        self.dictPathLabel.grid(row = 2, column=0, padx=10, pady=10)
        self.dictPath = Entry(self.tabSettings)
        self.dictPath.grid(row=2, column=1, columnspan=4, padx=10, pady=10, sticky='we')
        self.dictPathButton = Button(self.tabSettings, text="Browse", command=self.dictBrowseButton)
        self.dictPathButton.grid(row=2, column=5, padx=10, pady=10) 

        #search engine checkbuttons
        self.checkbuttonValues = {}

        self.checkbuttonValues["ip_v4"] = IntVar()
        self.ipv4Checkbutton = Checkbutton(self.tabSettings, variable=self.checkbuttonValues["ip_v4"], text='IP v4')
        self.ipv4Checkbutton.grid(row=3,column=0, padx=5,pady=5)
        self.ipv4Checkbutton.select()

        self.checkbuttonValues["ip_v6"] = IntVar()
        self.ipv6Checkbutton = Checkbutton(self.tabSettings, variable=self.checkbuttonValues["ip_v6"], text='IP v6')
        self.ipv6Checkbutton.grid(row=3,column=1, padx=5,pady=5)
        self.ipv6Checkbutton.select()
        
        self.checkbuttonValues['socialsec'] = IntVar()
        self.socialSecNumCheckbutton = Checkbutton(self.tabSettings, variable=self.checkbuttonValues["socialsec"], text='Socian sec num')
        self.socialSecNumCheckbutton.grid(row=3,column=2, padx=5,pady=5)
        self.socialSecNumCheckbutton.select()

        self.checkbuttonValues['id_number'] = IntVar()
        self.idNumCheckbutton = Checkbutton(self.tabSettings, variable=self.checkbuttonValues["id_number"], text='ID number')
        self.idNumCheckbutton.grid(row=3,column=3, padx=5,pady=5)
        self.idNumCheckbutton.select()

        self.checkbuttonValues['mac'] = IntVar()
        self.macCheckbutton = Checkbutton(self.tabSettings, variable=self.checkbuttonValues["mac"], text='MAC')
        self.macCheckbutton.grid(row=4,column=0, padx=5,pady=5)
        self.macCheckbutton.select()

        self.checkbuttonValues['domain'] = IntVar()
        self.domainCheckbutton = Checkbutton(self.tabSettings, variable=self.checkbuttonValues["domain"], text='Domains')
        self.domainCheckbutton.grid(row=4,column=1, padx=5,pady=5)
        self.domainCheckbutton.select()

        self.checkbuttonValues['email'] = IntVar()
        self.emailCheckbutton = Checkbutton(self.tabSettings, variable=self.checkbuttonValues["email"], text='Email')
        self.emailCheckbutton.grid(row=4,column=2, padx=5,pady=5)
        self.emailCheckbutton.select()

        self.checkbuttonValues['password'] = IntVar()
        self.passwordCheckbutton = Checkbutton(self.tabSettings, variable=self.checkbuttonValues["password"], text='Password')
        self.passwordCheckbutton.grid(row=4,column=3, padx=5,pady=5)
        self.passwordCheckbutton.select()

        self.checkbuttonValues['login'] = IntVar()
        self.loginCheckbutton = Checkbutton(self.tabSettings, variable=self.checkbuttonValues["login"], text='Logins')
        self.loginCheckbutton.grid(row=5,column=0, padx=5,pady=5)
        self.loginCheckbutton.select()

        self.checkbuttonValues['phone_number'] = IntVar()
        self.phoneNoCheckbutton = Checkbutton(self.tabSettings, variable=self.checkbuttonValues["phone_number"], text='Phone no.')
        self.phoneNoCheckbutton.grid(row=5,column=1, padx=5,pady=5)
        self.phoneNoCheckbutton.select()

        #not connected to values variable=self.checkbuttonValues[-1]
        self.dictionaryValue = IntVar()
        self.dictionaryCheckbutton = Checkbutton(self.tabSettings, variable=self.dictionaryValue, text='Dictionary')
        self.dictionaryCheckbutton.grid(row=5,column=2, padx=5,pady=5)
        self.dictionaryCheckbutton.select()

        self.additionalValue = IntVar()
        self.additionalCheckbutton = Checkbutton(self.tabSettings, variable=self.additionalValue, text='Additional')
        self.additionalCheckbutton.grid(row=5,column=3, padx=5,pady=5)
        
        #start/cancel/progress
        self.startButton = Button(self.tabSettings, command=self.startFunction, text="Start", background="green")
        self.startButton.grid(row=6, column=5, padx=5, pady=5)

        self.cancelButton = Button(self.tabSettings, command=self.cancelFunction, text="Cancel", background="red")
        self.cancelButton.grid(row=7, column=5, padx=5, pady=5)

        #info output elements
        self.progressbarValue = 0
        self.progressbar = ttk.Progressbar(self.tabSettings, orient="horizontal", length=500, mode="determinate", value=self.progressbarValue)
        self.progressbar.grid(row=6, column=0, padx=5, pady=5, columnspan=4)

        self.outputInfo = Label(self.tabSettings, text='...')
        self.outputInfo.grid(row=7, column=0, padx=5, pady=5, columnspan=4)

        #init results tab
        self.resultsList = Listbox(self.tabResults)
        self.resultsList.pack(fill=BOTH, expand=YES)

        self.scrollbar = Scrollbar(self.tabResults, orient=VERTICAL)
        self.scrollbar.config(command=self.resultsList.yview)
        self.scrollbar.pack(side="right", fill="y")

        self.resultsList.config(yscrollcommand=self.scrollbar.set)        
        self.resultsList.pack(side=LEFT,fill=BOTH)

        self.tabs.pack(expand=1, fill='both')


        #for Testing 
        self.inPath.insert(0, "C:\\Projects\\Thesis\\Code\\tests\\mailDump_100.json")
        self.outPath.insert(0, "C:\\Projects\\Thesis\\Code\\tests")


        self.cancel = False
        self.working = False

        self.window.mainloop()

    def inBrowseButton(self):
        filename = filedialog.askopenfilename()
        self.inPath.delete(0, END)
        self.inPath.insert(0, filename)

    def outBrowseButton(self):
        filename = filedialog.askdirectory()
        self.outPath.delete(0, END)
        self.outPath.insert(0, filename)

    def dictBrowseButton(self):
        filename = filedialog.askopenfilename()
        self.dictPath.delete(0, END)
        self.dictPath.insert(0, filename)

    def startFunction(self):
        self.progressbar['value'] = 0
        if self.working == False:
            self.working = True
            self.outputInfo['text'] = 'Creating parsing core'
            self.core = Core(self.progressbar)
            
            self.outputInfo['text'] = 'Initialising input parser'
            try:
                self.core.initInputParser(self.inPath.get())
            except Exception as x:
                self.displayException(x)
                self.outputInfo['text'] = "Couldn't open input path"
                self.cancelFunction()
                return

            self.outputInfo['text'] = 'Initialising output'
            try:
                self.core.initOutput(self.outPath.get())
            except Exception as x:
                self.displayException(x)
                self.outputInfo['text'] = "Couldn't open output"
                self.cancelFunction()
                return

            self.outputInfo['text'] = 'Initialising default regexes'
            try:
                self.core.initRegexes(self.checkbuttonValues)
            except Exception as x:
                self.displayException(x)
                self.outputInfo['text'] = "Couldn't initialize regexes"
                self.cancelFunction()
                return
            
            if self.additionalValue.get() == 1:
                self.outputInfo['text'] = 'Initialising additional regexes'
                try:
                    self.core.initAdditional()
                except Exception as x:
                    self.displayException(x)
                    self.outputInfo['text'] = "Failed to load additional regexes"
                    self.cancelFunction()
                    return

            if self.dictionaryValue.get() == 1:
                self.outputInfo['text'] = 'Initialising dictionary'
                try:
                    self.core.initDictionary(self.dictPath.get())
                except Exception as x:
                    self.displayException(x)
                    self.outputInfo['text'] = "Couldn't open dictionary path"
                    self.cancelFunction()
                    return

            self.outputInfo['text'] = 'Started parsing'
            self.core.start()

    def cancelFunction(self):
        if self.core != None:
            self.core.cancel = True
        self.working = False
        self.progressbar['value'] = 0

    def displayException(self, x):
        print("-"*15,"EXCEPTION","-"*15)
        print(type(x))
        print(x)
        print(traceback.format_exc())
        pass

    def __del__(self):
        if self.core != None:
            self.core.cancel = True



