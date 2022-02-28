from settings import *
import pygame

class Score:
    SCORE = 0
    def __init__(self,proportion,color):
        self.font = pygame.font.Font('font\Pixeltype.ttf',40)
        self.color = color
        self.image = self.font.render(str(self.SCORE),False,self.color)
        self.rect = self.image.get_rect(center =(WIDTH*proportion//4,50))
        
    def draw(self,screen):
        screen.blit(self.image,self.rect)
        
    def update(self,score_opp):
        if score_opp:
            self.SCORE += 1
            self.image = self.font.render(str(self.SCORE),False,self.color)
            
    def reset(self):
        self.SCORE = 0
        self.image = self.font.render(str(self.SCORE),False,self.color)
        
    def win(self):
        if self.SCORE == 5:
            return True