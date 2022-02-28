### HACER EL NUEVO MODO DE JUEGO
### RELAMPAGO: LA BOLA SE HACE MAS RAPIDO CADA VEZ (GRAVITY)
### PORTALES: CREA DOS PORTALES POR LOS QUE PASA LA PELOTA

import pygame
from normal_mode import *
from settings import *
import sys
from states import *
from menu import Menu
from controls import ControlsScreen

class Game:
    STATE = 'MENU'
    def __init__(self):
        pygame.init()
        self.WIDTH = WIDTH
        self.HEIGTH = HEIGTH
        self.screen = pygame.display.set_mode((self.WIDTH, self.HEIGTH))
        pygame.display.set_caption('PONG')
        self.running = True
        self.clock = pygame.time.Clock()
        pass
    
    def draw(self):
        pygame.display.update()
        self.clock.tick(FPS)
        self.screen.fill('#2c313c')
    
    def game(self):
        self.states()
        while self.running:
            self.event_loop()
            self.run_state()
            self.draw()
          
    def event_loop(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            self.run_loop_state(event)
            self.controls.exit_game(event)
                
    def run_state(self):
        if self.STATE == 'MENU':
            self.menu.draw(self.screen)
            
        if self.STATE == 'CONTROLS':
            self.controls.draw(self.screen)
            
        if self.STATE == 'COUNT':
            self.countdown.update(self.screen)
            self.countdown.draw(self.screen)
            self.countdown.normalmode.draw_game_assets(self.screen)
            
        if self.STATE == 'NORMAL MODE':
            self.normal_mode.draw_game_assets(self.screen)
            self.normal_mode.update()
            
        if self.STATE == 'PAUSE':
            self.normal_mode.draw_game_assets(self.screen)
            self.pause.score_point(self.screen)
        
        if self.STATE == 'WON1':
            self.player1_won.someone_won(self.screen)
        
        if self.STATE == 'WON2':
            self.player2_won.someone_won(self.screen)
            
    def states(self):
        self.menu = Menu(self)
        self.controls = ControlsScreen(self)
        self.normal_mode = NormalMode(self)
        self.countdown = Countdown(self,self.normal_mode)
        self.pause = Pause(self,self.normal_mode)
        self.player1_won = WinScreen(self,'PLAYER 1 WON!','#5ea3d1',self.normal_mode)
        self.player2_won = WinScreen(self,'PLAYER 2 WON!','#e06c75',self.normal_mode)
            
    def run_loop_state(self,event):
        if self.STATE == 'MENU':
            self.menu.event_loop(event)
           
        if self.STATE == 'NORMAL MODE':
            self.normal_mode.event_loop(event)
            
        if self.STATE == 'WON1' or self.STATE == 'WON2':
            self.normal_mode = NormalMode(self)
            self.player1_won.event_loop(event)
                   
if __name__ == '__main__':
    game = Game()
    game.game()
