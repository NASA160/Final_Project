import math

import pygame

from settings import *

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('PlayerSprites/white_square.png').convert_alpha()
        self.rect = self.image.get_rect()
        self.speed = 10
        self.direction = pygame.Vector2()

    def inputs(self):
        self.keys = pygame.key.get_pressed()
        self.direction.y = int(self.keys[pygame.K_DOWN]) - int(self.keys[pygame.K_UP])
        self.direction.x = int(self.keys[pygame.K_RIGHT]) - int(self.keys[pygame.K_LEFT])
        print(self.direction)
        # TODO optimize normilization
        # self.direction.normalize_ip()
        # if math.fabs(self.direction.y) and math.fabs(self.direction.x):
        #     self.direction.y *= (1/math.sqrt(2))
        #     self.direction.x *= (1/math.sqrt(2))


    def move(self, dt):
        self.rect.x += self.direction.x * self.speed
        self.rect.y += self.direction.y * self.speed

    def update(self, dt):
        self.inputs()
        self.move(dt)

