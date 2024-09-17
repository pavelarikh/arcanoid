import pygame

from settings import Settings


class Game():
    def __init__(self):
        pygame.init()
        self.settings = Settings()
        self.window = pygame.display.set_mode((self.settings.width_window, 
                                            self.settings.length_window))
        #pygame.display.set_caption(self.settings.name)
        self.window.fill(self.settings.backround_color)
        self.clock = pygame.time.Clock()
        self.running = True
        
    def event_handler(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
        
    def run(self):
        while self.running:
            self.window.fill(self.settings.backround_color)
            self.event_handler()
            self.clock.tick(self.settings.fps)
            pygame.display.update()
        
        
if __name__ == '__main__':
    game = Game()
    game.run()