import pygame
from cat import Cat


class Cat2(Cat):
    def __init__(self):
        self.case = 30
        self.catPositionX = 20
        self.catPositionY = 20
        self.catSize = 15
        self.mooveUnit = 40
        self.height = 35
        self.width = 35
        self.img = pygame.image.load('tom.png')
