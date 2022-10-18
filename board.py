import pygame

HEIGHT = 40
WIDTH = 40
COLOR1 = (0, 0, 0)
COLOR2 = (255, 255, 255)

class Board:
    def __init__(self):
        #print("The board of the game is getting create")
        self.case = []
        for r in range(20):
            row = []
            for l in range(20):
                row.append(0)
                self.case.append(row)

    def Draw(self,ecran):
        for row in range(20):
            for column in range(20):
                if (column + row) % 2 == 0:
                    rectangle = pygame.draw.rect(ecran, COLOR1 , [row * WIDTH, column * WIDTH, HEIGHT, WIDTH])
                else:
                    rectangle = pygame.draw.rect(ecran, COLOR2 , [row * WIDTH, column * WIDTH, HEIGHT, WIDTH])
