from re import S
from states import State
from text import *
from settings import *

class Menu(State):
    def __init__(self, game):
        super().__init__(game)
        self.game_type = Text(60,'GAMETYPES',self.game.WIDTH//2,180,'#d19a66')
        self.game_type1 = Text(40,'HUMAN VS HUMAN',self.game.WIDTH//2,240,'#c2626b')
        self.game_type2 = Text(40,'HUMAN VS AI (SOON)',self.game.WIDTH//2,280,'#c2626b')
        self.game_type3 = Text(40,'HUMAN VS HUMAN | ADD-ONS (SOON)',self.game.WIDTH//2,320,'#c2626b')
        self.game_name = Text(70,'WELCOME TO MY VERSION OF PONG',self.game.WIDTH//2,100,'#c678dd')
        self.controls_menu = Text(30,'CONTROLS',self.game.WIDTH//2,470)
        
    def draw(self,screen):
        self.game_type1.draw(screen)
        self.game_name.draw(screen)
        self.game_type2.draw(screen)
        self.game_type3.draw(screen)
        self.game_type.draw(screen)
        self.controls_menu.draw(screen)
    
    def event_loop(self,event):
        if event.type == pygame.MOUSEMOTION:
            if self.game_type1.rect.collidepoint(event.pos):
                self.game_type1.change_color('White')
            else:
                self.game_type1.change_color('#c2626b')
                
            if self.controls_menu.rect.collidepoint(event.pos):
                self.controls_menu.change_color('White')
            else:
                self.controls_menu.change_color('#5ea3d1')
                
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.game_type1.rect.collidepoint(event.pos):
                self.start_time = int(pygame.time.get_ticks())
                self.game.countdown.start_time = int(pygame.time.get_ticks())
                self.game.STATE = 'COUNT'
            if self.controls_menu.rect.collidepoint(event.pos):
                self.game.STATE = 'CONTROLS'
