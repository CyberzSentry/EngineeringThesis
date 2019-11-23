import re
import json
import os

regexLibPath = 'regexLib.json'

class Core:

    def __init__(self, regexList, dictionary=None):
        self.compiledRegexes = []
        with open(os.path.join(os.path.dirname(__file__), regexLibPath),'r') as rl:
            self.regexList = json.load(rl)
        for id in regexList:
            self.compiledRegexes.append(re.compile(self.regexList[id]))
        
    def match(self, content):
        for regex in self.compiledRegexes:
            print(regex.findall(content))