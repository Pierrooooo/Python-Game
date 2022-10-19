import pygame


class Difficulties:

    def __init__(self):
        self.lvlOfDif = "Easy"
        self.roundToWin = 20

    def SelectMode(self, difficultyChoosen):
        if difficultyChoosen == '1':
            self.lvlOfDif = "Easy"
            self.roundToWin = 20
        elif difficultyChoosen == '2':
            self.lvlOfDif = "Medium"
            self.roundToWin = 50
        elif difficultyChoosen == '3':
            self.lvlOfDif = "Hard"
            self.roundToWin = 100
        elif difficultyChoosen == '4':
            self.lvlOfDif = "Hard Core Extrem"
            self.roundToWin = 9999


