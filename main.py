import pygame
from pytmx.util_pygame import load_pygame

from Sprites import Sprite, CollisionSprite, TreeSprite
from groups import AllSprites
from inventory import inventory
from settings import *
from player import *
from inventory import *

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode(WINDOW_SIZE)
        self.clock = pygame.time.Clock()

        self.all_sprites = AllSprites()
        self.collision_sprites = pygame.sprite.Group()

        self.L1_tree_sprites = pygame.sprite.Group()
        self.L2_tree_sprites = pygame.sprite.Group()
        self.L3_tree_sprites = pygame.sprite.Group()
        self.L4_tree_sprites = pygame.sprite.Group()

        self.all_trees = [
            (self.L1_tree_sprites, 1),
            (self.L2_tree_sprites, 2),
            (self.L3_tree_sprites, 3),
            (self.L4_tree_sprites, 4),
        ]

        self.inventory = inventory(0, 0)


    def setup(self):
        map = load_pygame(os.path.join('data', 'Maps', 'Map1.tmx'))

        for x, y, image in map.get_layer_by_name('Water').tiles():
            Sprite((x * TILE_SIZE * SCALE_FACTOR, y * TILE_SIZE * SCALE_FACTOR), image, self.all_sprites)

        for x, y, image in map.get_layer_by_name('Ground').tiles():
            spr = Sprite((x * TILE_SIZE * SCALE_FACTOR, y * TILE_SIZE * SCALE_FACTOR), image, self.all_sprites)
            spr._is_ground = True  # <-- add this line
        for x, y, image in map.get_layer_by_name('Details').tiles():
            Sprite((x * TILE_SIZE * SCALE_FACTOR, y * TILE_SIZE * SCALE_FACTOR), image, self.all_sprites)

        for obj in map.get_layer_by_name('L1 Trees'):
            TreeSprite((obj.x * SCALE_FACTOR, obj.y * SCALE_FACTOR), obj.image, (self.all_sprites, self.collision_sprites, self.L1_tree_sprites))

        for obj in map.get_layer_by_name('L2 Trees'):
            TreeSprite((obj.x * SCALE_FACTOR, obj.y * SCALE_FACTOR), obj.image, (self.all_sprites, self.collision_sprites, self.L2_tree_sprites))

        for obj in map.get_layer_by_name('L3 Trees'):
            TreeSprite((obj.x * SCALE_FACTOR, obj.y * SCALE_FACTOR), obj.image, (self.all_sprites, self.collision_sprites, self.L3_tree_sprites))

        for obj in map.get_layer_by_name('L4 Trees'):
            TreeSprite((obj.x * SCALE_FACTOR, obj.y * SCALE_FACTOR), obj.image, (self.all_sprites, self.collision_sprites, self.L4_tree_sprites))

        for obj in map.get_layer_by_name('Entities'):
            if obj.name == "Player_Start":
                self.player = Player((obj.x * SCALE_FACTOR, obj.y * SCALE_FACTOR), self.all_sprites, self.collision_sprites)

        for obj in map.get_layer_by_name('Collisions'):
            CollisionSprite((obj.x * SCALE_FACTOR, obj.y * SCALE_FACTOR), pygame.Surface((int(obj.width), int(obj.height))), self.collision_sprites)



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

            self.inventory.check_collect(self.all_trees, self.all_sprites.get_offset())


            self.inventory.draw_all(self.screen, self.player.rect.center)

            pygame.display.flip()

        pygame.quit()





# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    game = Game()
    game.setup()
    game.run()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
