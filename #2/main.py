import pygame
from math import *

from config import *
from functions import *
from player import Player
from ray_casting import *
pygame.font.init()

display = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()
player = Player()
font = pygame.font.Font(None, 45)
pygame.mouse.set_visible(False)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()
    player.delta = delta_time()
    player.move()
    display.fill((0, 0, 0))

    pygame.draw.rect(display, (75,153,231), (0, 0, width, half_height))
    pygame.draw.rect(display, (18,18,18), (0, half_height, width, half_height))

    ray_casting(display, player)
    fps_text = font.render("FPS: " + str(int(clock.get_fps())), True, (250, 0, 0))
    display.blit(fps_text, (10, 10))

    # [pygame.draw.rect(display, pygame.Color("gray"), (x, y, block_size, block_size), 1) for x, y in block_map]
    #
    # pygame.draw.circle(display, pygame.Color("yellow"), (player.x, player.y), 10)

    clock.tick(0)
    pygame.display.flip()