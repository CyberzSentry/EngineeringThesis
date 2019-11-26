import os
import tkinter as Tk
from . import inputParser
from . import core 
from . import view


class Controller:



    def __init__(self):
        self.programView = view.View(self.test, self.run)

        #searchEngine = core.Core(['ip_v4', 'ip_v6'], None)
        #testFilePath = 'tests/test_data_0.json'
        #inPath = os.path.join(os.path.dirname(__file__), testFilePath)
    

    def test(self):
        Tk.messagebox.showinfo('Message title', 'Message content')


    def run(self, inPath):
        searchEngine = core.Core(['ip_v4', 'ip_v6'], None)
        with inputParser.Parser(inPath) as data:
            for d in data:
                print("Test ", d['id'], " ", d['content'])
                searchEngine.match(d['content'])