import pygame
from score import Score
from paddles import *
from ball import Ball
from text import Text

class State():
    def __init__(self,game):
        self.game = game
        pass
    
    def exit_game(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                self.game.STATE = 'MENU'
                
