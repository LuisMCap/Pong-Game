import pygame
from menu import Menu
from settings import *
import sys

class Game():
    def __init__(self) -> None:
        pygame.init()
        self.GAME_W,self.GAME_H = 480, 270
        self.WIDTH, self.HEIGTH = WIDTH, HEIGTH
        self.game_canvas = pygame.Surface((self.GAME_W,self.GAME_H))
        pygame.display.set_caption('PONG')
        self.running = True
        self.state_stack = []
        self.actions = {'start':False}
        self.screen = pygame.display.set_mode((self.WIDTH, self.HEIGTH))
        self.clock = pygame.time.Clock()
        self.load_states()
        
    def draw(self):
        pygame.display.update()
        self.clock.tick(FPS)
        self.screen.fill('#2c313c')
    
    def game_loop(self):
        while self.running:
            self.event_loop()
            self.draw()
            self.render()
            self.update()
            
    def event_loop(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
    
    def update(self):
        self.state_stack[-1].update(self.dt,self.actions)
                
    def render(self):
        self.state_stack[-1].draw(self.screen)
        # Render current state to the screen
        self.screen.blit(pygame.transform.scale(self.game_canvas,(self.WIDTH, self.HEIGTH)), (0,0))
        pygame.display.flip()
        
    def reset_keys(self):
        for action in self.actions:
            self.actions[action] = False
    
    def load_states(self):
        self.menu = Menu(self)
        self.state_stack.append(self.menu)
        
                
game = Game()
game.game_loop()