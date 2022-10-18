import pygame
import mouse


class Cat:
    def __init__(self):
        self.case = 30
        self.catPositionX = 780
        self.catPositionY = 780
        self.catColor = (255, 0, 0)
        self.catSize = 15

    #def Follow(self):
      #  print(mouse.mousePositionX)

    def Draw(self, ecran):
        pygame.draw.circle(ecran, self.catColor , (self.catPositionX, self.catPositionY), self.catSize)