import pygame

from settings import *
from player import *

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode(WINDOW_SIZE)
        self.clock = pygame.time.Clock()

        self.all_sprites = pygame.sprite.Group()
        self.player = Player()
        self.all_sprites.add(self.player)

    def run(self):
        running = True

        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
            self.dt = self.clock.tick(60) / 1000
            self.screen.fill((0, 0, 0))
            self.all_sprites.draw(self.screen)
            self.all_sprites.update(self.dt)
            pygame.display.flip()





# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    game = Game()
    game.run()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
