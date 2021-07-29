from math import *

import pygame.key

from config import *

class Player:
    def __init__(self):
        self.x = half_width
        self.y = half_height
        self.angle = 0
        self.delta = 0
        self.speed = 500
        self.ver_a = 0

    def move(self):
        key = pygame.key.get_pressed()
        cos_a, sin_a = cos(self.angle), sin(self.angle)

        if key[pygame.K_LEFT]:
            self.angle -= 3 * self.delta
        if key[pygame.K_RIGHT]:
            self.angle += 3 * self.delta
        if key[pygame.K_UP]:
            self.ver_a -= 1500 * self.delta
        if key[pygame.K_DOWN]:
            self.ver_a += 1500 * self.delta

        if key[pygame.K_w]:
            self.x += cos_a * self.delta * self.speed
            self.y += sin_a * self.delta * self.speed
        if key[pygame.K_s]:
            self.x -= cos_a * self.delta * self.speed
            self.y -= sin_a * self.delta * self.speed
        if key[pygame.K_a]:
            self.x += sin_a * self.delta * self.speed
            self.y -= cos_a * self.delta * self.speed
        if key[pygame.K_d]:
            self.x -= sin_a * self.delta * self.speed
            self.y += cos_a * self.delta * self.speed