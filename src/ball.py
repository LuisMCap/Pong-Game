import pygame
from settings import *
from random import choice

class Ball:
    def __init__(self,width, heigth ,x, y):
        self.rect = pygame.Rect(width, heigth ,x, y)
        self.heigth = heigth
        self.width = width
        self.x = x
        self.y = y
        self.gravity = 3
        self.movement_y = 6
        self.movement_x = 6
        
    def draw(self, screen):
        pygame.draw.ellipse(screen,'white',self.rect)
        
    def move(self):
        self.rect.x += self.movement_x
        self.rect.y += self.movement_y
        
    def boundaries(self):
        if self.rect.bottom >= HEIGTH or self.rect.top <= 0:
            self.movement_y *= -1
            
    def collision(self):
        self.movement_x *= -1
        
    def score_opponent(self):
        if self.rect.left <= -25:
            return True
        
    def score_player(self):
        if self.rect.right >= WIDTH+25:
            return True
        
    def update(self):
        self.move()
        self.boundaries()
        
    def new_point(self):
        if self.rect.right >= WIDTH+25 or self.rect.left <= -25:
            self.movement_y = 6 *choice([1,-1])
            self.movement_x = 6 *choice([1,-1])
    
    def restart_position(self):
        self.rect.center = (self.width,self.heigth)
        
    def kill(self):
        del self