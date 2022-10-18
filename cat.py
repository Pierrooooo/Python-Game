import pygame
import mouse


class Cat:
    def __init__(self):
        self.case = 30
        self.catPositionX = 780
        self.catPositionY = 780
        self.catColor = (255, 0, 0)
        self.catSize = 15
        self.mooveUnit = 40

    def Follow(self, mouse):
        print(mouse.mousePositionX)
        if mouse.mousePositionX >= self.catPositionX:
            self.catPositionX += self.mooveUnit
        else:
            self.catPositionX -= self.mooveUnit

        if mouse.mousePositionY >= self.catPositionY:
            self.catPositionY += self.mooveUnit
        else:
            self.catPositionY -= self.mooveUnit

    def Draw(self, ecran):
        pygame.draw.circle(ecran, self.catColor , (self.catPositionX, self.catPositionY), self.catSize)