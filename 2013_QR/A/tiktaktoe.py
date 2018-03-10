"""
Google Codejam 2013 Qualification Round; Problem A; Tik-Tak-Toe-Tomek
by DelkysWelffer
"""

def define_status(board):
    
    # look for winners rows
    for i in range(4):
        x_count_row = 0
        o_count_row = 0
        x_count_col = 0
        o_count_col = 0
        for j in range(4):
            if board[i][j] == 'X':
                x_count_row += 1
            elif board[i][j] == 'O':
                o_count_row += 1
            elif board[i][j] == 'T':
                x_count_row += 1
                o_count_row += 1

            if board[j][i] == 'X':
                x_count_col += 1
            elif board[j][i] == 'O':
                o_count_col += 1
            elif board[j][i] == 'T':
                x_count_col += 1
                o_count_col += 1
        if x_count_row == 4:
            return "X won"
        elif o_count_row == 4:
            return "O won"

        if x_count_col == 4:
            return "X won"
        elif o_count_col == 4:
            return "O won"
    
    # look in the principal diagonal
    x_count = 0
    o_count = 0
    for i in range(4):
        if board[i][i] == 'X':
            x_count += 1
        elif board[i][i] == 'O':
            o_count += 1
        elif board[i][i] == 'T':
            x_count += 1
            o_count += 1
    if x_count == 4:
        return "X won"
    elif o_count == 4:
        return "O won"

    # look in the secondary diagonal
    x_count = 0
    o_count = 0
    for i in range(4):
        if board[i][3 - i] == 'X':
            x_count += 1
        elif board[i][3 - i] == 'O':
            o_count += 1
        elif board[i][3 - i] == 'T':
            x_count += 1
            o_count += 1
    if x_count == 4:
        return "X won"
    elif o_count == 4:
        return "O won"

    for row in board: 
        if '.' in row: 
            return "Game has not completed"

    return "Draw"



if __name__ == "__main__":
    for T in range(1, int(input()) + 1):
        board = [list(input()) for _ in range(4)]
        print ("Case #{}: {}".format(T, define_status(board)))