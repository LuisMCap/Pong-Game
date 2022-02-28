from states import State
from text import *

class ControlsScreen(State):
    def __init__(self,game):
        super().__init__(game)
        self.player_controls = Text(40,'PLAYER 1',self.game.WIDTH//4,50,'#5ea3d1')
        self.opponent_controls = Text(40,'PLAYER 2',self.game.WIDTH*3//4,50,'#c2626b')

        self.player_controls1 = PromptText(35, 'W:  Move up',75,100,'#5ea3d1')
        self.player_controls2 = PromptText(35, 'S:  Move down',75,130,'#5ea3d1')

        self.opponent_controls1 = PromptText(35, 'Arrow key up:  Move up',400,100,'#c2626b')
        self.opponent_controls2 = PromptText(35, 'Arrow key down:  Move down',400,130,'#c2626b')

        self.win_text = Text(40, 'First Player to score 5 points wins!',self.game.WIDTH//2,410,'#d19a66')
        
    def draw(self, screen):
        self.player_controls.draw(screen)
        self.opponent_controls.draw(screen)
        
        pygame.draw.aaline(screen, (200,200,200),(self.game.WIDTH//2,0),(self.game.WIDTH//2,320))
        pygame.draw.aaline(screen, (200,200,200),(0,320),(self.game.WIDTH,320))
        
        self.player_controls1.draw(screen)
        self.player_controls2.draw(screen)
        
        self.opponent_controls1.draw(screen)
        self.opponent_controls2.draw(screen)
        
        self.win_text.draw(screen)
    