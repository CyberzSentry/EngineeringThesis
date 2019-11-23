#!/usr/bin/python3
import os
import searchEngine
from inputParser.Parser import Parser
from searchEngine.pythonCore.Core import Core

testFilePath = 'tests/test_data_0.json'
inPath = os.path.join(os.path.dirname(__file__), testFilePath)
searchEngine = Core(['ip_v4', 'ip_v6'], None)

with Parser(inPath) as data:
    for d in data:
        print("Test ", d['id'], " ", d['content'])
        searchEngine.match(d['content'])