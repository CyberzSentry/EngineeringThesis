import re
import json
import os
from threading import Thread
#from .inputParser import Parser
#test pack
import time

regexLibPath = 'regexLib.json'

class Core(Thread):

    def __init__(self, progressbar):
        Thread.__init__(self)
        self.cancel = False
        self.progressbar = progressbar
        
        # self.compiledRegexes = []
        # with open(os.path.join(os.path.dirname(__file__), regexLibPath),'r') as rl:
        #     self.regexList = json.load(rl)
        # for id in regexList:
        #     self.compiledRegexes.append(re.compile(self.regexList[id]))
    
    def initInputParser(self, path):
        # self.parser = Parser(path)
        pass

    def initDictionary(self, path):
        pass

    def initAdditional(self):
        pass

    def initRegexes(self):
        pass

    def initOutput(self):
        pass

    def run(self):
        while not self.cancel:
            self.progressbar['value'] += 1
            time.sleep(2)  
