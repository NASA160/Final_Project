from settings import *

class Player(pygame.sprite.Sprite):
    def __init__(self, pos, groups, collision_sprites):
        super().__init__(groups)
        self.load_images()
        self.state, self.frame_index = 'Down', 0
        self.image = pygame.image.load(os.path.join('PlayerSprites', 'Down', '0.png')).convert_alpha()
        self.image = pygame.transform.scale(self.image, (self.image.width * SCALE_FACTOR, self.image.height * SCALE_FACTOR))
        self.rect = self.image.get_rect(center = pos)
        self.hitbox_rect = self.rect

        self.speed = PLAYER_SPEED
        self.direction = pygame.Vector2()

        self.collision_sprites = collision_sprites

    def load_images(self):
        self.frames = {'Left': [], 'Right': [], 'Up': [], 'Down': []}
        base_dir = 'PlayerSprites'

        for state in self.frames.keys():
            state_path = os.path.join(base_dir, state)
            for folder_path, sub_folders, file_names in walk(state_path):
                if file_names:
                    clean_file_names = [
                        name for name in file_names
                        if not name.startswith('.') and name.split('.')[0].isdigit()
                    ]
                    sorted_file_names = sorted(
                        clean_file_names,
                        key=lambda name: int(name.split('.')[0])
                    )

                    for file_name in sorted_file_names:
                        full_path = os.path.join(folder_path, file_name)

                        try:
                            surf = pygame.image.load(full_path).convert_alpha()
                            self.frames[state].append(surf)
                        except pygame.error as e:
                            print(f"Error loading image {full_path}: {e}")


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

    def animate(self, dt):

        if self.direction.x != 0:
            self.state = 'Right' if self.direction.x > 0 else 'Left'
        if self.direction.y != 0:
            self.state = 'Down' if self.direction.y > 0 else 'Up'

        self.frame_index = self.frame_index + 5 * dt if self.direction else 0
        self.image = self.frames[self.state][int(self.frame_index) % len(self.frames[self.state])]
        self.image = pygame.transform.scale(self.image, (self.image.width * SCALE_FACTOR, self.image.height * SCALE_FACTOR))


    def update(self, dt):
        self.inputs()
        self.move(dt)
        self.animate(dt)

