from math import *

import pygame.key

from config import *

class Player:
    def __init__(self):
        self.x = half_width
        self.y = half_height
        self.angle = 0
        self.delta = 0
        self.speed = 450

    def move(self):
        key = pygame.key.get_pressed()
        cos_a, sin_a = cos(self.angle), sin(self.angle)

        self.mouse_control()
        if key[pygame.K_ESCAPE]:
            quit()

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

    def mouse_control(self):
        if pygame.mouse.get_focused():
            difference = pygame.mouse.get_pos()[0] - half_width
            pygame.mouse.set_pos((half_width, half_height))
            self.angle += difference * self.delta * 0.1