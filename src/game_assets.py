from states import State
import pygame
from score import Score
from paddles import *
from ball import Ball

class GameAssets(State):
    def __init__(self, game):
        super().__init__(game)
        self.player_score = Score(3)
        self.opponent_score = Score(1)
        self.left_paddle = Player(5,HEIGTH//2 - 35,10,70)
        self.right_paddle = Opponent(WIDTH-15,HEIGTH//2 - 35,10,70)
        self.ball = Ball(WIDTH//2, HEIGTH//2 ,10,10)
        
    def draw_game_assets(self,screen):
        self.left_paddle.draw(screen)
        self.right_paddle.draw(screen)
        self.ball.draw(screen)
        
        pygame.draw.aaline(screen, (200,200,200),(WIDTH//2,0),(WIDTH//2,HEIGTH))
        
        self.player_score.draw(screen)
        self.opponent_score.draw(screen)
        
    def hola(self):
        pass