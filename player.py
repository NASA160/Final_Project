from settings import *

class Player(pygame.sprite.Sprite):
    def __init__(self, pos, groups, collision_sprites):
        super().__init__(groups)
        self.image = pygame.image.load('PlayerSprites/idle copy.png').convert_alpha()
        self.image = pygame.transform.scale(self.image, (self.image.width * SCALE_FACTOR, self.image.height * SCALE_FACTOR))
        self.rect = self.image.get_frect(center = pos)
        self.speed = PLAYER_SPEED
        self.direction = pygame.Vector2()

    def inputs(self):
        self.keys = pygame.key.get_pressed()
        self.direction.y = int(self.keys[pygame.K_DOWN]) - int(self.keys[pygame.K_UP])
        self.direction.x = int(self.keys[pygame.K_RIGHT]) - int(self.keys[pygame.K_LEFT])
        self.direction = self.direction.normalize() if self.direction else self.direction

        self.speed = PLAYER_SPRINT_SPEED if self.keys[pygame.K_1] else PLAYER_SPEED

    def move(self, dt):
        self.rect.x += self.direction.x * self.speed
        self.rect.y += self.direction.y * self.speed

    def update(self, dt):
        self.inputs()
        self.move(dt)

