import pygame
from board import Board
from mouse import Mouse
from cat import Cat
from difficulties import Difficulties

module_charge = pygame.init()
difficultyChoosen = input("Choose your level of difficulty between 1 - 2 - 3 - 4: ")

ecran = pygame.display.set_mode([800, 800])
pygame.display.set_caption("Ecran Damier")

loop = True

board = Board()
mouse = Mouse()
cat = Cat()
difficulties = Difficulties()
difficulties.SelectMode(difficultyChoosen)

counter = 0

while loop:
    ecran.fill((0,0,0))

    for event in pygame.event.get() :
        if event.type == pygame.KEYDOWN:

            counter += 1

            if counter % 3 != 0:
                mouse.mooveUnit = 40
            else:
                mouse.mooveUnit = 80

            mouse.Moove(event)
            cat.Follow(mouse)

            if mouse.mousePositionX == cat.catPositionX and mouse.mousePositionY == cat.catPositionY:
                loop = False
                print(f'You loosed at the round N°{counter - 1}.')

            if counter == difficulties.roundToWin:
                loop = False
                print(f'You won on the {difficulties.lvlOfDif} difficulty mode')

            if event.key == pygame.K_j:
                loop = False
        if event.type == pygame.QUIT:
            loop = False

    board.Draw(ecran)
    mouse.Draw(ecran)
    cat.Draw(ecran)
    pygame.display.flip()