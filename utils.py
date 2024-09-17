import pygame


class Area():
    def __init__(self, x: int = 0, y: int = 0, width: int = 8, length: int = 24,
                 colour: tuple = (210, 180, 140)):
        self.rect = pygame.Rect(x, y, width, length)
        self.colour = colour
        self.x = x
        self.y = y
        
    def draw(self, window):
        pygame.draw.rect(window, self.colour, self.rect)
        
    def draw_outline(self, window):
        pygame.draw.rect(window, color=(230, 230, 250), rect=self.rect, width=5)
        
    def collidepoint(self, x, y):
        return self.rect.collidepoint(x, y)
    
        
class Picture(Area):
    def 