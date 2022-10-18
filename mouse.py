import pygame


class Mouse:
    def __init__(self):
        self.case = 30
        self.mousePositionX = 420
        self.mousePositionY = 420
        self.mouseColor = (47, 214, 120)
        self.mouseSize = 8
        self.mooveUnit = 40

    def Moove(self, event):
        if event.key == pygame.K_q or event.key == pygame.K_LEFT:
            if self.mousePositionX >= 40:
                self.mousePositionX -= self.mooveUnit
            else:
                self.mousePositionX = 20

        elif event.key == pygame.K_d or event.key == pygame.K_RIGHT:
            if self.mousePositionX <= 740:
                self.mousePositionX += self.mooveUnit
            else:
                self.mousePositionX = 780

        elif event.key == pygame.K_z or event.key == pygame.K_UP:
            if self.mousePositionY >= 40:
                self.mousePositionY -= self.mooveUnit
            else:
                self.mousePositionY = 20

        elif event.key == pygame.K_s or event.key == pygame.K_DOWN:
            if self.mousePositionY <= 740:
                self.mousePositionY += self.mooveUnit
            else:
                self.mousePositionY = 780



    def Draw(self, ecran):
        pygame.draw.circle(ecran, self.mouseColor, (self.mousePositionX, self.mousePositionY), self.mouseSize)