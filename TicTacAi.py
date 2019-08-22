import random


class TicTacAi:

        # TODO: 	Create a way to have easy,medium and hard ai
        #	   	Hard can be the ai that is used now
        #		Easy and medium can just have a random factor added in
        #		These will be decieded with the settigs param

    def __init__(self, settings):
        self.settings = settings

    def takeTurnAI(board):
        if(can_i_win(board) != -1):
            return can_i_win(board)
        elif (can_they_win(board) != -1):
            return can_they_win(board)
        elif (corner_open(board) != -1):
            return corner_open(board)
        elif(middle_open(board) != -1):
            return middle_open(board)
        elif(last_open(board) != -1):
            return last_open(board)
        else:
            print("Game should be a draw..... ENDING....")

# can_i_win checks to see if the ai has a winning move
# can_they_win checks to see if the player has a winning move
# corner_open checks to see if there is an open corner to take
# middle_open checks to to see if the middle is open if the corners are not
# last_open checks for any other moves if the first 2 are not valid


def can_i_win(board):
    return can_win(board, 2)


def can_they_win(board):
    return can_win(board, 1)


def corner_open(board):
    corners = [0, 2, 6, 8]
    for i in range(len(corners)):
        if(board[corners[i]] == 0):
            return corners[i]
    return -1


def middle_open(board):
    if(board[4] == 0):
        return 5
    return -1


def last_open(board):
    other = [1, 3, 5, 7]
    for i in range(len(other)):
        if(board[corners[i]] == 0):
            return other[i]
    return -1


def can_win(board, player):
        # Checks the rows for if the player can win by placing in an empty spot
        # then returns the empty spot
    for i in range(0, 3):
        if (checkRow(board, i * 3, player)):

            for j in range(0, 3):

                if (board[(i * 3) + j] == 0):

                    return (i * 3) + j
    # Checks the colomns for if the player can win by placing in an empty spot
        # then returns the empty spot
    for i in range(0, 3):
        if (checkColomn(board, i, player)):
            for j in range(0, 3):
                if (board[i + (3 * j)] == 0):
                    return i + (3 * j)
    # Checks the diags for if the player can win by placing in an empty spot
        # then returns the empty spot
    diag = checkDiag(board, player)
    if(diag[1]):
        for j in range(len(diag[0])):
            if(board[diag[0][j]] == 0):
                return diag[0][j]

    return -1


def checkRow(board, rowStart, player):
    count_one = 0
    for i in range(rowStart, (rowStart + 3)):
        if(board[i] == player):
            count_one += 1
    if(count_one == 2):
        return True
    else:
        return False


def checkColomn(board, colomnStart, player):
    count_one = 0
    for i in range(0, 3):
        if(board[colomnStart + (i * 3)] == player):
            count_one += 1
    if(count_one == 2):
        return True
    else:
        return False


def checkDiag(board, player):
    diag_one = [0, 4, 8]
    diag_two = [2, 4, 6]
    diag_count_one = 0
    diag_count_two = 0
    for i in range(0, 3):
        if(board[diag_one[i]] == player):
            diag_count_one += 1
        if(board[diag_two[i]] == player):
            diag_count_two += 1
    if(diag_count_one == 2):
        return [diag_one, True]
    elif (diag_count_two == 2):
        return [diag_two, True]
    else:
        return [None, False]
