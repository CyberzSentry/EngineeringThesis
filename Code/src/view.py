from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from tkinter import filedialog

class View:

    def __init__(self, testButton, startFunction):
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


        #over writing on value for the search engine
        self.ipv4Checkbutton = Checkbutton(self.tabSettings, text='IP v4')
        self.ipv4Checkbutton.grid(row=3,column=0, padx=5,pady=5)
        self.ipv4Checkbutton.select()

        self.ipv6Checkbutton = Checkbutton(self.tabSettings, text='IP v6')
        self.ipv6Checkbutton.grid(row=3,column=1, padx=5,pady=5)
        self.ipv6Checkbutton.select()

        self.socialSecNumCheckbutton = Checkbutton(self.tabSettings, text='Socian sec num')
        self.socialSecNumCheckbutton.grid(row=3,column=2, padx=5,pady=5)
        self.socialSecNumCheckbutton.select()

        self.idNumCheckbutton = Checkbutton(self.tabSettings, text='ID number')
        self.idNumCheckbutton.grid(row=3,column=3, padx=5,pady=5)
        self.idNumCheckbutton.select()

        self.macCheckbutton = Checkbutton(self.tabSettings, text='MAC')
        self.macCheckbutton.grid(row=4,column=0, padx=5,pady=5)
        self.macCheckbutton.select()

        self.domainCheckbutton = Checkbutton(self.tabSettings, text='Domains')
        self.domainCheckbutton.grid(row=4,column=1, padx=5,pady=5)
        self.domainCheckbutton.select()

        self.emailCheckbutton = Checkbutton(self.tabSettings, text='MAC')
        self.emailCheckbutton.grid(row=4,column=2, padx=5,pady=5)
        self.emailCheckbutton.select()

        self.passwordCheckbutton = Checkbutton(self.tabSettings, text='Password')
        self.passwordCheckbutton.grid(row=4,column=3, padx=5,pady=5)
        self.passwordCheckbutton.select()

        self.loginCheckbutton = Checkbutton(self.tabSettings, text='Logins')
        self.loginCheckbutton.grid(row=5,column=0, padx=5,pady=5)
        self.loginCheckbutton.select()

        self.phoneNoCheckbutton = Checkbutton(self.tabSettings, text='Phone no.')
        self.phoneNoCheckbutton.grid(row=5,column=1, padx=5,pady=5)
        self.phoneNoCheckbutton.select()

        self.dictionaryCheckbutton = Checkbutton(self.tabSettings, text='Dictionary')
        self.dictionaryCheckbutton.grid(row=5,column=2, padx=5,pady=5)
        self.dictionaryCheckbutton.select()

        self.additionalCheckbutton = Checkbutton(self.tabSettings, text='Additional')
        self.additionalCheckbutton.grid(row=5,column=3, padx=5,pady=5)
        
        #start/cancel/progress
        self.startButton = Button(self.tabSettings, text="Start", background="green")
        self.startButton.grid(row=5, column=5, padx=5, pady=5)

        self.cancelButton = Button(self.tabSettings, text="Cancel", background="red")
        self.cancelButton.grid(row=6, column=5, padx=5, pady=5)

        self.progressbar = ttk.Progressbar(self.tabSettings, orient="horizontal", length=500, mode="determinate")
        self.progressbar.grid(row=6, column=0, padx=5, pady=5, columnspan=4)

        #init results tab
        self.resultsList = Listbox(self.tabResults)
        self.resultsList.pack(fill=BOTH, expand=YES)

        self.scrollbar = Scrollbar(self.tabResults, orient=VERTICAL)
        self.scrollbar.config(command=self.resultsList.yview)
        self.scrollbar.pack(side="right", fill="y")

        self.resultsList.config(yscrollcommand=self.scrollbar.set)
        
        # for i in range(100):
        #     self.resultsList.insert(END, str(i))
        self.resultsList.pack(side=LEFT,fill=BOTH)

        self.tabs.pack(expand=1, fill='both')
        self.window.mainloop()


    def displayMessage(self, title, message):
        messagebox.showinfo(title, message)

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


#test start for test
view = View(None, None)