from TicTacAi import TicTacAi
import msvcrt as m


class TURN(enumerate):
    player_one = 1
    player_two = 2

    def nextTurn(turn):
        player_one = 1
        player_two = 2
        if (turn == player_one):
            return player_two
        else:
            return player_one


def main():
    runGame()


def runGame():
    # instantiate board
    #   000  123  012
    #   000  456  345
    #   000  789  678
    board = [0, 0, 0, 0, 0, 0, 0, 0, 0]   # blank board

    # TEST BOARDS
    # board = [1, 1, 1, 0, 0, 0, 0, 0, 0] # p1 top row win
    # board = [0, 0, 0, 1, 1, 1, 0, 0, 0] # p1 middle row win
    # board = [0, 0, 0, 0, 0, 0, 1, 1, 1] # p1 bottom row win
    # board = [1, 0, 0, 1, 0, 0, 1, 0, 0] # p1 left colomn win
    # board = [0, 1, 0, 0, 1, 0, 0, 1, 0] # p1 middle colomn win
    # board = [0, 0, 1, 0, 0, 1, 0, 0, 1] # p1 right colomn win
    # board = [1, 0, 0, 0, 1, 0, 0, 0, 1] # p1 neg diag win
    # board = [0, 0, 1, 0, 1, 0, 1, 0, 0] # p1 pos diag win
    # board = [1, 2, 1, 2, 1, 2, 2, 1, 2] # draw board

    # turn can equal either 1 or 2 for the players


    settings = 0
    ai = TicTacAi
    ai.settings = settings
    ai_play = True
    turn = TURN.player_one
    game_over = [False, False]  # Is the game over and was it a draw

    game_over = checkGameOver(board)

    while not(game_over[0]):
        showBoard(board)
        board = takeTurn(board, turn, ai_play, ai)
        turn = TURN.nextTurn(turn)
        game_over = checkGameOver(board)
    showBoard(board)
    gameOver(turn, game_over[1])


def takeTurn(board, turn, ai_play, ai):
    print("Player: " + str(turn) + " Enter where you would like to move.")
    print("Please use 1 - 9 to select")
    print("EX. Enter 5 to move to (2, 2) aka the middle")
    if (ai_play and (turn == TURN.player_two)):
        move_spot = ai.takeTurnAI(board)
        board[move_spot] = turn
        return board
    else:
        move_spot = input()

    if(str.isnumeric(move_spot)):
        move_spot = int(move_spot)
    else:
        print("Number 1 - 9 not entered. Try again.\n")
        showBoard(board)
        takeTurn(board, turn, ai_play, ai)
        return board

    if(board[move_spot - 1] == 0):
        board[move_spot - 1] = turn
    else:
        print("Invalid move. Try picking a blank space.\n")
        showBoard(board)
        takeTurn(board, turn, ai_play, ai)
        return board
    return board



def checkGameOver(board):
    for i in range(0, 3):
        if (checkRow(board, i * 3)):
            return [True, False]
    for i in range(0, 3):
        if (checkColomn(board, i)):
            return [True, False]
    for i in range(1, 3):
        if(checkDiag(board, i)):
            return [True, False]
    for i in range(len(board)):
        if(board[i] == 0):
            return [False, False]

    return [True, True]


def checkRow(board, rowStart):
    count_one = 0
    count_two = 0
    for i in range(rowStart, (rowStart + 3)):
        if(board[i] == 1):
            count_one += 1
        if(board[i] == 2):
            count_two += 1
    if((count_one == 3) or (count_two == 3)):
        return True
    else:
        return False


def checkColomn(board, colomnStart):
    count_one = 0
    count_two = 0
    for i in range(0, 3):
        if(board[colomnStart + (i * 3)] == 1):
            count_one += 1
        if(board[colomnStart + (i * 3)] == 2):
            count_two += 1
    if((count_one == 3) or (count_two == 3)):
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
    if((diag_count_one == 3) or (diag_count_two == 3)):
        return True
    else:
        return False


def gameOver(turn, was_draw):
    if(was_draw):
        print("Draw")
        print("Press any key to continue....")
        wait()
        exit()
    else:
        turn = TURN.nextTurn(turn)
        print("Player " + str(turn) + " Wins!")
        print("Press any key to continue....")
        wait()
        exit()


def showBoard(board):
    result = ""
    reversed_board = board[::-1]
    for i in range(9):
        if((i % 3) == 0):
            result += XorO(board[i])
        elif((i % 3) == 1):
            result += XorO(board[i])
        else:
            result += XorO(board[i]) + "\n"
    print(result)


def XorO(inNum):
    if (inNum == 1):
        return "O "
    elif (inNum == 2):
        return "X "
    else:
        return "_ "


def wait():
    m.getch()

if __name__ == '__main__':
    main()
