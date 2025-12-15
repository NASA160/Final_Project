from settings import *

class Player(pygame.sprite.Sprite):
    def __init__(self, pos, groups, collision_sprites):
        super().__init__(groups)
        self.image = pygame.image.load(os.path.join('PlayerSprites', 'idle copy.png')).convert_alpha()
        self.image = pygame.transform.scale(self.image, (self.image.width * SCALE_FACTOR, self.image.height * SCALE_FACTOR))
        self.rect = self.image.get_frect(center = pos)
        self.hitbox_rect = self.rect
        self.speed = PLAYER_SPEED
        self.direction = pygame.Vector2()

        self.collision_sprites = collision_sprites

    def inputs(self):
        self.keys = pygame.key.get_pressed()
        self.direction.y = int(self.keys[pygame.K_DOWN]) - int(self.keys[pygame.K_UP])
        self.direction.x = int(self.keys[pygame.K_RIGHT]) - int(self.keys[pygame.K_LEFT])
        self.direction = self.direction.normalize() if self.direction else self.direction

        self.speed = PLAYER_SPRINT_SPEED if self.keys[pygame.K_1] else PLAYER_SPEED

    def move(self, dt):
        self.rect.x += self.direction.x * self.speed * dt
        self.collision('horizontal')
        self.rect.y += self.direction.y * self.speed * dt
        self.collision('vertical')

    def collision(self, direction):
        for sprite in self.collision_sprites:
            # sprite.rect = sprite.rect.inflate(-50, -50)
            if sprite.rect.colliderect(self.hitbox_rect):
                if direction == 'horizontal':
                    if self.direction.x > 0: self.hitbox_rect.right = sprite.rect.left
                    if self.direction.x < 0: self.hitbox_rect.left = sprite.rect.right
                if direction == 'vertical':
                    if self.direction.y > 0: self.hitbox_rect.bottom = sprite.rect.top
                    if self.direction.y < 0: self.hitbox_rect.top = sprite.rect.bottom

    def update(self, dt):
        self.inputs()
        self.move(dt)

