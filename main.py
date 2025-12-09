import pygame
from pytmx.util_pygame import load_pygame

from Sprites import Sprite, CollisionSprite
from groups import AllSprites
from settings import *
from player import *

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode(WINDOW_SIZE)
        self.clock = pygame.time.Clock()

        self.all_sprites = AllSprites()
        self.collision_sprites = pygame.sprite.Group()


    def setup(self):
        map = load_pygame('data/Maps/Map1.tmx')

        for x, y, image in map.get_layer_by_name('Water').tiles():
            Sprite((x * TILE_SIZE * SCALE_FACTOR, y * TILE_SIZE * SCALE_FACTOR), image, self.all_sprites)

        for x, y, image in map.get_layer_by_name('Ground').tiles():
            Sprite((x * TILE_SIZE * SCALE_FACTOR, y * TILE_SIZE * SCALE_FACTOR), image, self.all_sprites)

        for x, y, image in map.get_layer_by_name('Details').tiles():
            Sprite((x * TILE_SIZE * SCALE_FACTOR, y * TILE_SIZE * SCALE_FACTOR), image, self.all_sprites)

        for obj in map.get_layer_by_name('Trees'):
            CollisionSprite((obj.x * SCALE_FACTOR, obj.y * SCALE_FACTOR), obj.image, (self.all_sprites, self.collision_sprites))

        for obj in map.get_layer_by_name('Entities'):
            if obj.name == "Player_Start":
                self.player = Player((obj.x * SCALE_FACTOR, obj.y * SCALE_FACTOR), self.all_sprites, self.collision_sprites)



    def run(self):
        running = True

        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
            self.dt = self.clock.tick(60) / 1000
            self.screen.fill((0, 0, 0))
            self.all_sprites.draw(self.player.rect.center)
            self.all_sprites.update(self.dt)
            pygame.display.flip()

        pygame.quit()





# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    game = Game()
    game.setup()
    game.run()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
