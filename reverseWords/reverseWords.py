"""
reverseWords.py
"""

from sys import argv

filename = argv[1]

def readN(thefile):
    return int(thefile.readline())

def readWords(thefile, N):
    lines = [[] for x in range(N)]
    word = ""
    i = 0
    for i in range(N):
        line = thefile.readline()
        for ch in line:
            if ch == ' ':
                lines[i].append(word)
                word = ''
            elif ch == '\n':
                lines[i].append(word)
                #lines.append([])
                word = ''
                i += 1
            else:
                word += ch
    return lines

def readWords2(thefile, N):
    lines = [thefile.readline().strip('\n').split(' ') for x in range(N)]
    print(lines)

def reverse(phrase):
    reversePhrase = []
    for x in range(-1, -len(phrase) - 1, -1):
        reversePhrase.append(phrase[x])
    return reversePhrase

def reverseAll(phrases):
    lines = []
    line = ''
    for phrase in phrases:
        if len(phrase) == 1:
            lines.append(phrase[0])
            continue
        phrase = phrase.reverse()
        for word in phrase:
            line += word + ' '
        lines.append(line)
        line = ''
    return lines


if __name__ == "__main__":

    thefile = open(filename, 'r')
    newfile = open('output', 'w')

    N = readN(thefile)
    
    thewords = readWords2(thefile, N)

    reverseWords = reverseAll(thewords)

    print(thewords)
    print(reverseWords)

    i = 1
    for phrase in reverseWords:
        print("Case #{0}: {1}".format(i, phrase), file = newfile)
        i += 1

    thefile.close()
