import re
import json
import os
from threading import Thread
import time

class Parser:
    def __init__(self, inputPath):
        self.inPath = inputPath
        self.count = -1
        with open(inputPath, 'r') as inFile:
            self.inData = json.load(inFile)
        self.len = len(self.inData['messages'])
        self.done = False

    def __enter__(self):
        return self.inData['messages']

    def __exit__(self, type, value, traceback):
        pass

    def getNext(self):
        """returns next element from the input file"""
        self.count += 1
        if self.len > self.count:
            return self.inData['messages'][self.count]
        else:
            self.done = True
            return None

class Core(Thread):

    def __init__(self, progressbar):
        Thread.__init__(self)
        self.cancel = False
        self.progressbar = progressbar
        self.compiledRegexes = []
        # with open(os.path.join(os.path.dirname(__file__), regexLibPath),'r') as rl:
        #     self.regexList = json.load(rl)
        # for id in regexList:
        #     self.compiledRegexes.append(re.compile(self.regexList[id]))
    
    def initInputParser(self, path):
        print("\n-----------------------Initialising input parser----------------------\n")
        self.parser = Parser(path)
        pass

    def initDictionary(self, path):
        pass

    def initAdditional(self, additionalLibPath='regexLib.json'):
        print("\n--------------------Initialising additional regexes-------------------\n")
        if additionalLibPath == 'regexLib.json':
            additionalLibPath = os.path.join(os.path.dirname(__file__), additionalLibPath)
        with open(additionalLibPath,'r') as rl:
            self.additionalList = json.load(rl)['additional']
            for x in self.additionalList:
                reg = self.additionalList[x]['regex']
                if reg is not '':
                    print("Init regex ", x, " ", reg)
                    self.compiledRegexes.append(reg)
                else:
                    print("Regex empty, not compiling")

    def initRegexes(self, checkbuttonValues=None, regexLibPath='regexLib.json'):
        print("\n-------------------------Initialising regexes-------------------------\n")
        if regexLibPath == 'regexLib.json':
            regexLibPath = os.path.join(os.path.dirname(__file__), regexLibPath)
        with open(regexLibPath,'r') as rl:
            self.regexList = json.load(rl)['main']
            if checkbuttonValues is not None:
                for x, y in checkbuttonValues.items():
                    if y.get() == 1:
                        reg = self.regexList[x]['regex']
                        if reg is not '':
                            print("Init regex ", x, " ", reg)
                            self.compiledRegexes.append(reg)
                        else:
                            print("Regex empty, not compiling")    
            else:
                for x in self.regexList:
                    reg = self.regexList[x]['regex']
                    if reg is not '':
                        print("Init regex ", x, " ", reg)
                        self.compiledRegexes.append(reg)
                    else:
                        print("Regex empty, not compiling")


    def initOutput(self):
        pass

    def run(self):
        while not self.cancel:
            self.progressbar['value'] += 1
            time.sleep(2)
