import pygame

pygame.init()

window = pygame.display.set_mode((500,500))
pygame.display.set_caption("TicTacToe")

run = True

while run:
    doEvent()
    doLogic()
    doRender()
pygame.quit()



def doEvent():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

def doLogic():
    return

def doRender():
    pygame.display.update()