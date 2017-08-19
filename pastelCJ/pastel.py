
options = {
    'up-r': [-1, 1],
    'up-l': [-1, -1],
    'down-r': [1, 1],
    'down-l': [1, -1]
    'up': [-1, 0],
    'down': [1, 0],
    'rigth': [0, 1],
    'left': [0, -1]
    }

def quedan_celdas_vacias(some_cake, R, C):
    for i in range(R):
        for j in range(C):
            if some_cake[i][j] is '?':
                return True
    return False


T = int(input())

for testcase in range(T):
    R, C = input().split(' ')
    R, C = int(R), int(C)
    cake = []
    for row in range(R):
        # cake.append([])
        cake.append(list(input()))

    # printing the cake
    for row in cake: print (row)

    cont = 0
    while quedan_celdas_vacias(cake, R, C):
        for i in range(R):
            for j in range(C):
                if cake[i][j] >= 'A' and cake[i][j] <= 'Z':
                    let = cake[i][j]
                    
