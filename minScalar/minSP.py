"""
minSP.py

Problem from Google Codejam Round 1A 2008

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
