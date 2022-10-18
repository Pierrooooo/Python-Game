import pygame

catColor = (255, 0, 0)
catPosition = (780, 780)
catSize = 15

class Cat:
    def __int__(self):
        self.case = 30

    def Draw(self, ecran):
        cat = pygame.draw.circle(ecran,catColor , catPosition, catSize)