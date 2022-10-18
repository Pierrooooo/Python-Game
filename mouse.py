import pygame

mouseColor = (47, 214, 120)
mousePosition = (20, 20)
mouseSize = 8

class Mouse:
    def __int__(self):
        self.case = 30

    def Draw(self, ecran):
        cat = pygame.draw.circle(ecran,mouseColor , mousePosition, mouseSize)