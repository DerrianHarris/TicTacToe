import pygame
from pygame.locals import *
import time
from TicTacAi import TicTacAi
window_size = (500,500)



#TODO: CLEAN CODE!

pygame.init()
window = pygame.display.set_mode(window_size)
pygame.display.set_caption("TicTacToe")


Turn = 0
board = [0, 0, 0, 0, 0, 0, 0, 0, 0]
ai = TicTacAi
run = True
isGameOver = [False,False]


def doEvent():
    global isGameOver
    global Turn
    global board
    global run

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            
            run = False
            
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and isGameOver[0] == False:
            print ("You pressed the left mouse button at (%d, %d)" % event.pos)
            w,h  = pygame.display.get_surface().get_size()
            x,y = event.pos

            cellPos =  (int(x / (w/3)),int(y / (h/3)))

            if(PlaceSpot(cellPos)):
                return
            else:
                return
        elif event.type == pygame.KEYDOWN and event.key == pygame.locals.K_r:
            print("Reseting Game..")
            

            Turn = 0
            board = [0, 0, 0, 0, 0, 0, 0, 0, 0]
            isGameOver = [False,False]
        elif event.type == pygame.KEYDOWN and event.key == pygame.locals.K_ESCAPE:
            run = False

def doLogic():
    global board
    global isGameOver
    isGameOver = checkGameOver(board)
    #if(isGameOver[0]):
    #    if(isGameOver[1]):
    #        print("Draw!")
    #    else:
    #        Player = (Turn + 1 ) % 2
    #        print("Player " + str(Player+1) + " Wins!")
    if(Turn == 1 and not isGameOver[0]):
        spot = ai.takeTurnAI(board)
        if(spot != -1):
            board[spot] = 2
            NextTurn()
    

def doRender():
    window.fill((200,200,200))
    w,h  = pygame.display.get_surface().get_size()

    pygame.draw.line(window,(0,0,0),(int(w/3),0),(int(w/3),h))
    pygame.draw.line(window,(0,0,0),(int(w/3) * 2,0),(int(w/3) * 2,h))
    pygame.draw.line(window,(0,0,0),(0,int(h/3)),(w,int(h/3)))
    pygame.draw.line(window,(0,0,0),(0,int(h/3) * 2),(w,int(h/3) * 2))
    font = pygame.font.SysFont("comicsansms",100)
    for i in range(9):
        x = int(i % 3)
        y = int(i / 3)
        offset = ((w/6),(h/6))
        choice = ""

        if board[i] == 0:
            continue
        elif board[i] == 1:
            choice = "O"
        elif board[i] == 2:
            choice = "X"
        
        text = font.render(choice,True,(0,0,0))
        pos = (int((x*(w/3)) + offset[0]),int((y*(h/3)) + offset[1]))
        textRect = text.get_rect()
        textRect.center = pos
        pygame.display.get_surface().blit(text,textRect)
    
    if isGameOver[0]:
        color = (255,0,0)
        if not isGameOver[1]:
            Player = (Turn + 1 ) % 2
            textStr = "Player %d Wins!" % (Player + 1)

            if Player == 1:
                color = (0,255,0)
            else:
                color = (0,0,255)
        else:
            textStr = "Draw"


        font = pygame.font.SysFont("comicsansms",70)
        text = font.render(textStr,True,color)
        pos = (w/2,h/2)
        textRect = text.get_rect()
        textRect.center = pos
        pygame.display.get_surface().blit(text,textRect)

        font = pygame.font.SysFont("comicsansms",40)
        text = font.render("Press R to reset...",True,color)
        pos = (w/2,(h/2) + 70)
        textRect = text.get_rect()
        textRect.center = pos
        pygame.display.get_surface().blit(text,textRect)

    pygame.display.update()


    
def PlaceSpot(Pos):
    x,y = Pos
    index = y * 3 + x
    #print (index)
    if board[index] == 0:
        board[index] = Turn + 1
        NextTurn()
        return True
    else:
        return False

def NextTurn():
    global Turn
    Turn = (Turn + 1) % 2
    print(Turn)
    
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


while run:
    doEvent()
    doLogic()
    doRender()
pygame.quit()
try:
    exit()
except:
    print("An exception occurred.")

