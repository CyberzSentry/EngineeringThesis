import re
import json
import os
from threading import Thread
import time
import shutil
import importlib
from importlib import machinery

class Parser:
    def __init__(self, inputPath):
        self.inPath = inputPath
        self.count = -1
        with open(inputPath, 'r') as inFile:
            self.inData = json.load(inFile)

        self.len = len(self.inData['messages'])
        self.stepValue = int(self.len/100)
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
        self.output = {}
        # with open(os.path.join(os.path.dirname(__file__), regexLibPath),'r') as rl:
        #     self.regexList = json.load(rl)
        # for id in regexList:
        #     self.compiledRegexes.append(re.compile(self.regexList[id]))
    
    def initInputParser(self, path):
        print("\n-----------------------Initialising input parser----------------------\n")
        self.inputPath = path
        self.parser = Parser(path)
        pass

    def initDictionary(self, path):
        print("\n------------------------Initialising dictionary-----------------------\n")
        self.dictionaryPath = path
        pass

    def initAdditional(self, additionalRegexLibPath='regexLib.json', additionalCodeLibpath='codeLib.py'):
        """Throws key KeyError when the input file structure is incorrect"""
        print("\n--------------------Initialising additional regexes-------------------\n")
        if additionalRegexLibPath == 'regexLib.json':
            additionalRegexLibPath = os.path.join(os.path.dirname(__file__), additionalRegexLibPath)

        self.additionalRegexLibPath = additionalRegexLibPath

        if additionalCodeLibpath == 'codeLib.py':
            loader = machinery.SourceFileLoader('codeLib', os.path.join(os.path.dirname(__file__),additionalCodeLibpath))
            self.additionalCodeModule = loader.load_module()
            #self.codeModule = importlib.import_module(codeLibPath[:-3], os.path.dirname(__file__))
        else:
            loader = machinery.SourceFileLoader(os.path.basename(additionalCodeLibpath[:-3]), additionalCodeLibpath)
            self.additionalCodeModule = loader.load_module()

        with open(additionalRegexLibPath,'r') as rl:
            self.additionalList = json.load(rl)['additional']
            for x in self.additionalList:
                reg = self.additionalList[x]['regex']
                funct = self.regexList[x]['code']
                if reg is not '':
                    print("Init regex ", x, " ", reg)
                    if funct is not '':
                        self.compiledRegexes.append([re.compile(reg), getattr(self.additionalCodeModule, funct), x])
                    else:
                        self.compiledRegexes.append([re.compile(reg), None, x])
                else:
                    print("Regex empty, not compiling")

    def initRegexes(self, checkbuttonValues=None, regexLibPath='regexLib.json', codeLibPath='codeLib.py'):
        """Throws key KeyError when the input file structure is incorrect"""
        print("\n-------------------------Initialising regexes-------------------------\n")
        if regexLibPath == 'regexLib.json':
            regexLibPath = os.path.join(os.path.dirname(__file__), regexLibPath)
        self.regexPath = regexLibPath

        if codeLibPath == 'codeLib.py':
            loader = machinery.SourceFileLoader('codeLib', os.path.join(os.path.dirname(__file__),codeLibPath))
            self.codeModule = loader.load_module()
            #self.codeModule = importlib.import_module(codeLibPath[:-3], os.path.dirname(__file__))
        else:
            loader = machinery.SourceFileLoader(os.path.basename(codeLibPath[:-3]), codeLibPath)
            self.codeModule = loader.load_module()
        self.codeLibPath = codeLibPath

        with open(regexLibPath,'r') as rl:
            self.regexList = json.load(rl)['main']
            if checkbuttonValues is not None:
                for x, y in checkbuttonValues.items():
                    if y.get() == 1:
                        reg = self.regexList[x]['regex']
                        funct = self.regexList[x]['code']
                        if reg is not '':
                            print("Init regex ", x, " ", reg)
                            if funct is not '':
                                self.compiledRegexes.append([re.compile(reg), getattr(self.codeModule, funct), x])
                            else:
                                self.compiledRegexes.append([re.compile(reg), None, x])
                        else:
                            print("Regex empty, not compiling")  
            else:
                for x in self.regexList:
                    reg = self.regexList[x]['regex']
                    funct = self.regexList[x]['code']
                    if reg is not '':
                        print("Init regex ", x, " ", reg)
                        if funct is not '':
                            self.compiledRegexes.append([re.compile(reg), getattr(self.codeModule, funct), x])
                        else:
                            self.compiledRegexes.append([re.compile(reg), None, x])
                    else:
                        print("Regex empty, not compiling")


    def initOutput(self, path, backup=True):
        print("\n--------------------------Initialising output-------------------------\n")
        fullPath = os.path.join(path, "output.json")
        self.outputFile = open(fullPath, "a")
        self.outputPath = fullPath
        if backup:
            shutil.copy(self.inputPath, os.path.join(path, "input_backup.json"))


    def run(self):

        for regex in self.compiledRegexes:
            self.output[regex[2]] = {"no": 0, "results": {}}

        x = 0
        while not self.cancel:
            content = self.parser.getNext()

            if content is None:
                break

            x+=1
            if x == self.parser.stepValue:
                self.progressbar['value'] += 1
                x=0
            
            for regex in self.compiledRegexes:
                results = regex[0].findall(content['content'])
                for result in results:
                    if regex[1] is not None:
                        if regex[1](result):
                            self.addOutput(regex[2], result, content['id'])
                    else:
                        self.addOutput(regex[2], result, content['id'])

        print(self.output)

    def addOutput(self, regex, result, id):
        if result in self.output[regex]["results"]:
            self.output[regex]["results"][result]["occurances"].append(id)
        else:
            self.output[regex]["results"][result] = {"occurances": [id]}
            self.output[regex]["no"] += 1