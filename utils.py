import pygame

   
class Area():
    def __init__(self, x=0, y=0, width=10, height=10, color='black'):
        self.rect = pygame.Rect(x, y, width, height)
        self.fill_color = color
            
    def color(self, new_color):
        self.fill_color = new_color
        
    def fill(self, window):
        pygame.draw.rect(window, self.fill_color, self.rect)
        
    def collidepoint(self, x, y):
        return self.rect.collidepoint(x, y) 
        
    def colliderect(self, rect):
        return self.rect.colliderect(rect)
 
 
class Label(Area):
    def set_text(self, text, fsize=12, text_color=(0, 0, 0)):
        self.image = pygame.font.SysFont('verdana', fsize).render(
            text, True, text_color)
        
    def draw(self, window, shift_x=0, shift_y=0):
        self.fill()
        window.blit(self.image, (self.rect.x + shift_x, self.rect.y + shift_y))

 
class Picture(Area):
    def __init__(self, filename, x=0, y=0, width=10, height=10):
        Area.__init__(self, x=x, y=y, width=width, height=height, color=None)
        self.image = pygame.image.load(filename)

    def draw(self, window):
        window.blit(self.image, (self.rect.x, self.rect.y))