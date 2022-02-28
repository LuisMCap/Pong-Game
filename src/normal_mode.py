from states import *

class GameAssets(State):
    def __init__(self, game):
        super().__init__(game)
        self.player_score = Score(3,'#c2626b')
        self.opponent_score = Score(1,'#5ea3d1')
        self.left_paddle = Player(5,HEIGTH//2 - 35,10,70,'#5ea3d1')
        self.right_paddle = Opponent(WIDTH-15,HEIGTH//2 - 35,10,70,'#c2626b')
        self.ball = Ball(WIDTH//2, HEIGTH//2 ,10,10)
        
        self.pause = pygame.USEREVENT + 0   
        
    def draw_game_assets(self,screen):
        self.player_score.draw(screen)
        self.opponent_score.draw(screen)
        
        self.left_paddle.draw(screen)
        self.right_paddle.draw(screen)
        self.ball.draw(screen)
        
        pygame.draw.aaline(screen, (200,200,200),(WIDTH//2,0),(WIDTH//2,HEIGTH))
        
    def restart_time(self):
        self.start_time = int(pygame.time.get_ticks())

class NormalMode(GameAssets):
    def __init__(self, game):
        self.pause_prompt = Text(30,'Press space to play a new point',WIDTH//2,400)
        super().__init__(game)
        
    def restart_time(self):
        self.start_time = int(pygame.time.get_ticks())
    
    def update(self):
        self.score_opp = self.ball.score_opponent()
        self.score_player = self.ball.score_player()
        
        self.left_paddle.update()      
        self.right_paddle.update()
        self.ball.update()
        
        self.player_score.update(self.score_opp)       
        self.opponent_score.update(self.score_player)
        self.win_player, self.win_opponent = self.player_score.win(), self.opponent_score.win()
        
        if self.score_opp or self.score_player:
            self.new_point()
            
        self.win_player, self.win_opponent = self.player_score.win(), self.opponent_score.win()
        
        self.collision_ball_paddle()
        self.who_won()
        
    def collision_ball_paddle(self):
        if self.left_paddle.rect.colliderect(self.ball.rect) or self.right_paddle.rect.colliderect(self.ball.rect):
            self.ball.collision()
            
    def new_point(self):
        pygame.event.post(pygame.event.Event(self.pause))
        self.ball.new_point()
        self.ball.restart_position()
        self.right_paddle.new_point()
        self.left_paddle.new_point()
        
    def event_loop(self,event):
        if event.type == self.pause:
            self.game.STATE = 'PAUSE'
            
    def draw(self, screen):
        self.player_score.draw(screen)
        self.opponent_score.draw(screen)
        
    def who_won(self):
        if self.win_player:
            self.game.STATE = 'WON2'
        if self.win_opponent:
            self.game.STATE = 'WON1'
        
class Countdown(State):
    def __init__(self, game, normalmode):
        super().__init__(game)
        self.normalmode = normalmode
        self.start_time = int(pygame.time.get_ticks())
        self.normalmode.ball.restart_position()
                 
    def draw(self, screen):
        self.countdown_text1.draw(screen)
        self.countdown_text.draw(screen)
            
    def update(self, screen):
        self.current_time = pygame.time.get_ticks() - self.start_time + 3
        self.countdown_text = Text(150,str(int(self.current_time/1000)),WIDTH//4,HEIGTH//2,'#5ea3d1')      
        self.countdown_text1 = Text(150,str(int(self.current_time/1000)),WIDTH*3//4,HEIGTH//2,'#c2626b') 
        if self.current_time >= 3000:
            go_text = Text(200,'GO!',WIDTH//2,HEIGTH//2)
            go_text.draw(screen)
            
        if self.current_time >= 3500:
            self.game.STATE = 'NORMAL MODE'     
        
class Pause(State):
    def __init__(self, game, normalmode):
        super().__init__(game)
        self.normalmode = normalmode
        self.pause_prompt = Text(30,'Press space to play a new point',WIDTH//2,400)
        
    def score_point(self,screen):
        self.normalmode.pause_prompt.draw(screen)
        self.normalmode.ball.restart_position()
        self.normalmode.ball.new_point()
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            self.game.STATE = 'NORMAL MODE'
    
    def draw(self,screen):
        self.normalmode.player_score.draw(screen)
        self.normalmode.opponent_score.draw(screen)
        self.normalmode.left_paddle.draw(screen)
        self.normalmode.right_paddle.draw(screen)
        self.normalmode.ball.draw(screen)
        
        pygame.draw.aaline(screen, (200,200,200),(WIDTH//2,0),(WIDTH//2,HEIGTH))
        
class WinScreen(GameAssets):
    def __init__(self, game, who_won,color,normalmode):
        super().__init__(game)
        self.normalmode = normalmode
        self.menu_prompt = Text(30,'PRESS SPACE OR ESC TO GO BACK TO THE MENU',WIDTH//2,400,'#d19a66')
        self.win_player = who_won
        self.color = color
        
    def someone_won(self, screen):
        won_text = Text(60,self.win_player,WIDTH//2,225,self.color)   
        won_text.draw(screen)
        self.menu_prompt.draw(screen)
        self.normalmode.opponent_score.reset()
        self.normalmode.player_score.reset()
        
    def event_loop(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                self.start_time = int(pygame.time.get_ticks())
                self.opponent_score.reset()
                self.player_score.reset()
                self.game.STATE = 'MENU'
                
        