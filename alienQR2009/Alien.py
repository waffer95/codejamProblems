"""
Alien.py
This is code for Qualification Round of Codejam 2009
This problem is the one that's about an alien language that has been discovered 
at Google Labs and so on...
"""

from sys import argv
import re

filename = argv[1]

def readLDN(_file):
    s = _file.readline()
    l = [int(i) for i in s.split(' ')]
    return l

def readWords(_file, leng, n_words):
    words = []
    for i in range(n_words):
        words.append(_file.readline().strip('\n'))
    return words

def readTestCases(_file, n_cases):
    test_cases = []
    for i in range(n_cases):
        test_cases.append(_file.readline().strip('\n'))
    return test_cases

def create_dictCases(cases):
    dict_cases = {}
    for i in range(len(cases)):
        dict_cases[str(i + 1)] = 0
    return dict_cases

def tokenize(case):
    pattern = r''
    for c in case:
        if c == '(':
            pattern += '['
        elif c == ')':
            pattern += ']'
        else:
            pattern += c
    return pattern

def analyze(_file, cases, words):
    dict_cases = create_dictCases(cases)
    pattern = ''
    for i in range(len(cases)):
        pattern = re.compile(tokenize(cases[i]))
        for word in words:
            if pattern.match(word):
                dict_cases[str(i + 1)] += 1
    return dict_cases


if __name__ == "__main__":
    f = open(filename, 'r', newline = '')
    l, d, n = readLDN(f)
    words = readWords(f, l, d)
    cases = readTestCases(f, n)
    
    print (l, d, n)
    print (words)
    print (cases)
    cases = analyze(f, cases, words)
    newfile = open('output.dat', 'w')
    for i in range(len(cases)):
        newfile.write("Case #{0}: {1}\n".format(i + 1, cases[str(i + 1)]))
    f.close()
