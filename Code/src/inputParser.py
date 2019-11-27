import json

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

    