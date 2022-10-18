import pygame
from board import Board
from mouse import Mouse
from cat import Cat

module_charge = pygame.init()
print(module_charge)

ecran = pygame.display.set_mode([800, 800])
pygame.display.set_caption("Ecran Damier")

loop = True

board = Board()
mouse = Mouse()
cat = Cat()

while loop:
    ecran.fill((0,0,0))


    for event in pygame.event.get() :
        if event.type == pygame.KEYDOWN:
            mouse.Moove(event)

            #cat.Follow(mouse.mousePositionX)
            if event.key == pygame.K_j:
                loop = False
        if event.type == pygame.QUIT:
            loop = False

    board.Draw(ecran)
    mouse.Draw(ecran)
    cat.Draw(ecran)
    pygame.display.flip()