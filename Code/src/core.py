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
        with open(inputPath, 'r',encoding='utf-8') as inFile:
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

    def __init__(self, inputPath, outputPath, expectedRegexes=None, data=None, dictionaryPath=None, progressEvent=None, updateDataEvent=None, finishedEvent=None, additional=True):
        Thread.__init__(self)
        self.cancel = False
        self.dictionarySearch = False
        print("\n-----------------------Initialising input parser----------------------\n")
        self.inputPath = inputPath
        self.parser = Parser(inputPath)
        print("\n--------------------------Initialising output-------------------------\n")
        self.outputFile = open(outputPath, "w")
        self.outputPath = outputPath

        
        self.compiledRegexes = []
        if dictionaryPath is not None:
            self.initDictionary(dictionaryPath=dictionaryPath)
        
        if additional:
            self.initAdditional()

        self.initRegexes(expectedRegexes=expectedRegexes)

        if data is None:
            self.output = {}
        else:
            self.output = data

        if progressEvent is not None:
            self.progressEvent = progressEvent
        else:
            self.progressEvent = self.dummy
        if updateDataEvent is not None:
            self.updateDataEvent = updateDataEvent
        else:
            self.updateDataEvent = self.dummy
        if finishedEvent is not None:
            self.finishedEvent = finishedEvent
        else:
            self.finishedEvent = self.dummy

    def initAdditional(self, additionalRegexLibPath='regexLib.json', additionalCodeLibpath='codeLib.py'):
        """Throws key KeyError when the input file structure is incorrect"""
        print("\n--------------------Initialising additional regexes-------------------\n")
        if additionalRegexLibPath == 'regexLib.json':
            additionalRegexLibPath = os.path.join(os.path.dirname(__file__), additionalRegexLibPath)

        self.additionalRegexLibPath = additionalRegexLibPath

        if additionalCodeLibpath == 'codeLib.py':
            loader = machinery.SourceFileLoader('codeLib', os.path.join(os.path.dirname(__file__),additionalCodeLibpath))
            self.additionalCodeModule = loader.load_module()
        else:
            loader = machinery.SourceFileLoader(os.path.basename(additionalCodeLibpath[:-3]), additionalCodeLibpath)
            self.additionalCodeModule = loader.load_module()

        with open(additionalRegexLibPath,'r') as rl:
            self.additionalList = json.load(rl, encoding='utf-8')['additional']
            for x in self.additionalList:
                reg = self.additionalList[x]['regex']
                funct = self.additionalList[x]['code']
                if reg is not '':
                    print("Init regex ", x, " ", reg)
                    if funct is not '':
                        self.compiledRegexes.append([re.compile(reg), getattr(self.additionalCodeModule, funct), x])
                    else:
                        self.compiledRegexes.append([re.compile(reg), None, x])
                else:
                    print("Regex empty, not compiling")

    def initRegexes(self, expectedRegexes=None, regexLibPath='regexLib.json', codeLibPath='codeLib.py'):
        """Throws key KeyError when the input file structure is incorrect"""
        print("\n-------------------------Initialising regexes-------------------------\n")
        if regexLibPath == 'regexLib.json':
            regexLibPath = os.path.join(os.path.dirname(__file__), regexLibPath)
        self.regexPath = regexLibPath

        if codeLibPath == 'codeLib.py':
            loader = machinery.SourceFileLoader('codeLib', os.path.join(os.path.dirname(__file__),codeLibPath))
            self.codeModule = loader.load_module()
        else:
            loader = machinery.SourceFileLoader(os.path.basename(codeLibPath[:-3]), codeLibPath)
            self.codeModule = loader.load_module()
        self.codeLibPath = codeLibPath

        with open(regexLibPath,'r') as rl:
            self.regexList = json.load(rl)['main']
            if expectedRegexes is not None:
                for x in expectedRegexes:
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

    def initDictionary(self,dictionaryPath, regexLibPath='regexLib.json'):
        print("\n------------------------Initialising dictionary-----------------------\n")
        if regexLibPath == 'regexLib.json':
            regexLibPath = os.path.join(os.path.dirname(__file__), regexLibPath)
        self.dictRegexPath = regexLibPath
        self.dictionaryPath = dictionaryPath
        self.dictionary = {}
        self.dictionarySearch = True
        with open(self.dictionaryPath, "r", encoding='utf-8') as f:
            for line in f:
                self.dictionary[line.strip()] = None

        self.dictionaryCompiledRegexes = []
        with open(regexLibPath,'r') as rl:
            self.dictionaryRegexList = json.load(rl)['dictionary']
            for x in self.dictionaryRegexList:
                reg = self.dictionaryRegexList[x]['regex']
                if reg is not '':
                    print("Init dictionary regex ", x, " ", reg)
                    self.dictionaryCompiledRegexes.append([re.compile(reg), x])
                else:
                    print("Regex empty, not compiling")

    def run(self):

        if self.dictionarySearch:
            for regex in self.compiledRegexes:
                self.output[regex[2]] = {"no": 0, "results": {}}
            for regex in self.dictionaryCompiledRegexes:
                self.output[regex[1]] = {"no": 0, "results": {}}
            x = 0
            while not self.cancel:
                content = self.parser.getNext()

                if content is None:
                    break

                x+=1
                if x == self.parser.stepValue:
                    self.progressEvent()
                    x=0
                
                for regex in self.compiledRegexes:
                    results = regex[0].findall(content['content'])
                    for result in results:
                        if regex[1] is not None:
                            if regex[1](result, content['content']):
                                self.addOutput(regex[2], result, content['id'])
                        else:
                            self.addOutput(regex[2], result, content['id'])
                
                for dictRegex in self.dictionaryCompiledRegexes:
                    results = dictRegex[0].findall(content['content'])
                    for result in results:
                        if result.lower() in self.dictionary:
                            self.addOutput(dictRegex[1], result, content['id'])
        else:
            for regex in self.compiledRegexes:
                self.output[regex[2]] = {"no": 0, "results": {}}
            x = 0
            while not self.cancel:
                content = self.parser.getNext()

                if content is None:
                    break

                x+=1
                if x == self.parser.stepValue:
                    self.progressEvent()
                    x=0
                
                for regex in self.compiledRegexes:
                    results = regex[0].findall(content['content'])
                    for result in results:
                        if regex[1] is not None:
                            if regex[1](result, content['content']):
                                self.addOutput(regex[2], result, content['id'])
                        else:
                            self.addOutput(regex[2], result, content['id'])

        self.finishedEvent()
        json.dump(self.output, self.outputFile)
        self.outputFile.close()

    def addOutput(self, regex, result, id):
        if result in self.output[regex]["results"]:
            self.output[regex]["results"][result]["occurances"].append(str(id))
        else:
            self.output[regex]["results"][result] = {"occurances": [str(id)]}
            self.output[regex]["no"] += 1
        self.updateDataEvent()

    def dummy(self):
        pass

    ###Implement destructor that backups data