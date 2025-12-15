
from settings import *

class Sprite(pygame.sprite.Sprite):
    def __init__(self, pos, surf, groups):
        super().__init__(groups)
        self.image = surf
        self.image = pygame.transform.scale(self.image, (self.image.width * SCALE_FACTOR, self.image.height * SCALE_FACTOR))
        self.rect = self.image.get_frect(topleft = pos)

class CollisionSprite(pygame.sprite.Sprite):
    def __init__(self, pos, surf, groups):
        super().__init__(groups)
        self.image = surf
        self.image = pygame.transform.scale(self.image, (self.image.width * SCALE_FACTOR, self.image.height * SCALE_FACTOR))
        self.rect = self.image.get_frect(topleft = pos)

class TreeSprite(pygame.sprite.Sprite):
    def __init__(self, pos, surf, groups):
        super().__init__(groups)
        self.image = surf
        self.image = pygame.transform.scale(self.image, (self.image.width * SCALE_FACTOR, self.image.height * SCALE_FACTOR))
        self.rect = self.image.get_frect(topleft = pos)
