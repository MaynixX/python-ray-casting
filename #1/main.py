import pygame
from math import *

from config import *
from functions import *
from player import Player

display = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()
player = Player()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()
    player.delta = delta_time()
    player.move()
    display.fill((0, 0, 0))

    pygame.draw.rect(display, (75,153,231), (0, 0, width, half_height - player.ver_a))
    pygame.draw.rect(display, (18,18,18), (0, half_height - player.ver_a, width, half_height + player.ver_a))

    ray_casting(display, player)

    # [pygame.draw.rect(display, pygame.Color("gray"), (x, y, block_size, block_size), 1) for x, y in block_map]
    #
    # pygame.draw.circle(display, pygame.Color("yellow"), (player.x, player.y), 10)

    pygame.display.set_caption("FPS: " + str(int(clock.get_fps())))
    clock.tick(0)
    pygame.display.flip()