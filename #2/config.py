from math import *
import pygame

# Экран
width = 1200
height = 800
half_width = width / 2
half_height = height / 2

# Карта
block_size = 100
text_map = ["11111111111111111",
            "1....111111.....1",
            "1...............1",
            "1............2111",
            "1...............1",
            "1111............1",
            "1...............1",
            "1.......2....1111",
            "1..22...........1",
            "1...............1",
            "1.1111..........1",
            "11111111111111111"
            ]
map_width = len(text_map[0])
map_height = len(text_map)

block_map_textures = {}
block_map = set()
y_block_pos = 0
for row in text_map:
    x_block_pos = 0
    for column in list(row):
        if column != ".":
            block_map.add((x_block_pos, y_block_pos))
            block_map_textures[(x_block_pos, y_block_pos)] = column
        x_block_pos += block_size
    y_block_pos += block_size

# Ray Casting
FOV = pi / 2
half_FOV = FOV / 2
max_depth = width // block_size
num_rays =  600
delta_ray = FOV / (num_rays - 1)
dist = num_rays / (2 * tan(half_FOV))
scale = width // num_rays
coefficient = dist * block_size * scale

# Текстуры
texture_size = 1024
texture_scale = texture_size // block_size
textures = {"1": pygame.image.load("textures/1.png"), "2": pygame.image.load("textures/2.jpg")}

# Миникарта
mini_map_coeff = 5
mini_map_width, mini_map_height = width // mini_map_coeff, height // mini_map_coeff