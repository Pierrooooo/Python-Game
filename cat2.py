import pygame



class Cat2:
    def __init__(self):
        self.case = 30
        self.catPositionX = 20
        self.catPositionY = 20
        self.catColor = (255, 0, 0)
        self.catSize = 15
        self.mooveUnit = 40

    def Follow(self, mouse):

        if mouse.mousePositionX >= self.catPositionX:
            self.catPositionX += self.mooveUnit
        else:
            self.catPositionX = self.catPositionX

        if mouse.mousePositionX <= self.catPositionX:
            self.catPositionX -= self.mooveUnit
        else:
            self.catPositionX = self.catPositionX

        if mouse.mousePositionY >= self.catPositionY:
            self.catPositionY += self.mooveUnit
        else:
            self.catPositionY = self.catPositionY

        if mouse.mousePositionY <= self.catPositionY:
            self.catPositionY -= self.mooveUnit
        else:
            self.catPositionY = self.catPositionY

    def Draw(self, ecran):
        pygame.draw.circle(ecran, self.catColor, (self.catPositionX, self.catPositionY), self.catSize)