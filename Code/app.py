#!/usr/bin/python3
import os
import searchEngine

testFilePath = 'tests/test_data_0.txt'

print(os.path.dirname(__file__))
print(os.path.join(os.path.dirname(__file__), testFilePath))
inputData = open(os.path.join(os.path.dirname(__file__), testFilePath),'r')
print(inputData)