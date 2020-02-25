import pygame

window_size = (500,500)

board = [1, 0, 0, 0, 2, 0, 0, 0, 1]

pygame.init()
window = pygame.display.set_mode(window_size)
pygame.display.set_caption("TicTacToe")
run = True
font = pygame.font.SysFont("comicsansms",100)

def doEvent():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            pygame.quit()
            quit()

def doLogic():
    return

def doRender():
    window.fill((200,200,200))
    w,h  = pygame.display.get_surface().get_size()

    pygame.draw.line(window,(0,0,0),(w/3,0),(w/3,h))
    pygame.draw.line(window,(0,0,0),((w/3) * 2,0),((w/3) * 2,h))
    pygame.draw.line(window,(0,0,0),(0,h/3),(w,h/3))
    pygame.draw.line(window,(0,0,0),(0,(h/3) * 2),(w,(h/3) * 2))
    
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

    pygame.display.update()


    





while run:
    doEvent()
    doLogic()
    doRender()



