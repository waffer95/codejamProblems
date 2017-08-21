"""
    cake.py

    Problem from Google Codejam 2017 Round 1A; Alphabet Cake

"""

def has_empty_cells(some_cake, R, C):
    for i in range(R):
        for j in range(C):
            if some_cake[i][j] is '?':
                return True
    return False

def is_empty_row(row):
    is_empty = True
    for elem in row:
        if elem is not '?':
            is_empty = False
    return is_empty

def dist_cake(cake, R, C):
    #while has_empty_cells(cake, R, C):
    #print ("Entrando en el ciclo 'while has_empty_cells(cake, R, C)'")
    # searching for letters in the cake
    for i in range(R):
        for j in range(C):
            if cake[i][j] >= 'A' or cake[i][j] <= 'Z':
                # sustituing from the letter to the right
                for jj in range(j + 1, C):
                    if cake[i][jj] is '?':
                        cake[i][jj] = cake[i][j]
                    elif cake[i][jj] is not cake[i][j] and cake[i][jj] is not '?':
                        break
                # sustituing from the letter to the left
                for jj in range(j, -1, -1):
                    if cake[i][jj] is '?':
                        cake[i][jj] = cake[i][j]
                    elif cake[i][jj] is not cake[i][j] and cake[i][jj] is not '?':
                        break

    while has_empty_cells(cake, R, C):
        # searching for the last empty row since the first row forward
        last_empty_row = None
        for i in range(R):
            if is_empty_row(cake[i]):
                last_empty_row = i
                break

        # searching for a non-empty row after the last_empty_row
        last_non_empty_row = None
        for i in range(last_empty_row, R):
            if not(is_empty_row(cake[i])):
                last_non_empty_row = i
                break

        # debug printing
        print ("X" * 5,"CAKE", "X" * 5)
        for row in cake:
            print (row)

        if last_empty_row is not None:
            print ("there is a empty row at", last_empty_row)
            if last_empty_row is R - 1:
                if is_empty_row(cake[last_empty_row - 1]):
                    for jj in range(C):
                        cake[last_empty_row][jj] = cake[last_empty_row - 2][jj]
                else:
                    for jj in range(C):
                        cake[last_empty_row][jj] = cake[last_empty_row - 1][jj]
            else:
                for jj in range(C):
                    cake[last_empty_row][jj] = cake[last_empty_row + 1][jj]
        else:
            print ("there is not a empty row at", last_empty_row)
        
    return cake



T = int(input())

for testcase in range(1, T + 1):
    R, C = input().split(' ')
    R, C = int(R), int(C)
    cake = []
    for row in range(R):
        cake.append(list(input()))

    # distributing the cake 
    cake = dist_cake(cake, R, C)

    # printing test cases
    print ("Case #{0}:".format(testcase))
    for row in cake:
        for cell in row:
            print (cell, end='')
        print ()