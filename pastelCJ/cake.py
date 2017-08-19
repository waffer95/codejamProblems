"""
    cake.py

    Problem from Google Codejam 2017 Round 1A; Alphabet Cake

"""


# options = {
#     'up-r': [-1, 1],
#     'up-l': [-1, -1],
#     'down-r': [1, 1],
#     'down-l': [1, -1]
#     'up': [-1, 0],
#     'down': [1, 0],
#     'rigth': [0, 1],
#     'left': [0, -1]
#     }


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
    while has_empty_cells(cake, R, C):
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
        for i in range(R):
            if is_empty_row(cake[i][:]):
                if i > 0:
                    for jj in range(C):
                        cake[i][jj] = cake[i - 1][jj]
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