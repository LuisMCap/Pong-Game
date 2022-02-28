import pygame
from settings import *

class Paddle:
    def __init__(self,width, heigth, x,y, color):
        self.x = x
        self.y = y
        self.width = width
        self.heigth = heigth
        self.rect = pygame.Rect(width, heigth ,x,y)
        self.speed = 8
        self.color = color
        
    def draw(self,screen):
        pygame.draw.rect(screen,self.color,self.rect)
            
    def boundaries(self):
        if self.rect.bottom >= HEIGTH-5:
            self.rect.bottom = HEIGTH-5
        if self.rect.top <= 5:
            self.rect.top = 5
            
    def new_point(self):
        self.rect = pygame.Rect(self.width, self.heigth ,self.x,self.y)

class Player(Paddle):
    def __init__(self,width, heigth, x,y,color):
        super().__init__(width, heigth, x, y,color)
        
    def user_input(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            self.rect.bottom -= self.speed
        if keys[pygame.K_s]:
            self.rect.bottom += self.speed
    
    def update(self):
        self.user_input()
        self.boundaries()
        
class Opponent(Paddle):
    def __init__(self,width, heigth, x,y,color):
        super().__init__(width, heigth, x, y,color)
        
    def user_input(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            self.rect.bottom -= self.speed
        if keys[pygame.K_DOWN]:
            self.rect.bottom += self.speed
                  
    def update(self):
        self.user_input()
        self.boundaries()