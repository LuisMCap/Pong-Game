import pygame

class Text:
    def __init__(self, font_size, desired_text,x ,y, color = (200,200,200)):
        self.font = pygame.font.Font('font\Pixeltype.ttf',font_size)
        self.color = color
        self.desired_text = desired_text
        self.image = self.font.render(self.desired_text,False,self.color)
        self.rect = self.image.get_rect(center=(x,y))
        pass
    
    def draw(self, screen):
        screen.blit(self.image,self.rect)
        
    def change_color(self,color):
        self.image = self.font.render(self.desired_text,False,color)
        
class PromptText(Text):
    def __init__(self, font_size, desired_text, x, y,color =(200,200,200)):
        super().__init__(font_size, desired_text, x, y,color)
        self.image = self.font.render(self.desired_text,False,self.color)
        self.rect = self.image.get_rect(midleft=(x,y))