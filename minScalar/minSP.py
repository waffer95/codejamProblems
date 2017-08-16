"""
minSP.py

problem from Google Codejam Round 1A 2008

I use here a new approach for the inputs

They have been asked to the user but I input the data
from the input files from the cli like this

python program.py < input.dat

I was surprised when I found out that you can do this! :) 


"""



N = int(input())

for testcase in range(1, N + 1):
    n = int(input())
    x = input().split(' ')
    y = input().split(' ')
    if len(x) != len(y):
        print("wrong!")
        break
    for i in range(n):
        x[i] = int(x[i])
        y[i] = int(y[i])
    x.sort()
    y.sort()
    y.reverse()
    suma = 0
    for i in range(n):
        suma += x[i] * y[i]
    print ("Case #{0}: {1}".format(testcase, suma))
