import pygame



class Cat:
    def __init__(self):
        self.case = 30
        self.catPositionX = 780
        self.catPositionY = 780
        self.catColor = (255, 0, 0)
        self.catSize = 15
        self.mooveUnit = 40
        self.height = 35
        self.width = 35
        self.img = pygame.image.load('tom.png')

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
        ecran.blit(self.img.convert_alpha(), ((self.catPositionX - self.width / 2 , self.catPositionY - self.height / 2)))
        #pygame.draw.circle(ecran, self.catColor , (self.catPositionX, self.catPositionY), self.catSize)