import pygame
from math import *

from config import *

texture = pygame.image.load("textures/1.png")
def ray_casting(display, player):
    in_block_pos = {'left': player.x - player.x // block_size * block_size,
                    'top': player.y - player.y // block_size * block_size,
                    'right': block_size - (player.x - player.x // block_size * block_size),
                    'bottom': block_size - (player.y - player.y // block_size * block_size)}

    for ray in range(num_rays):
        cur_angle = player.angle - half_FOV + delta_ray * ray
        cos_a, sin_a = cos(cur_angle), sin(cur_angle)
        vd, hd = 0, 0
        founded = False
        texture_v, texture_h = 0, 0


        # Вертикали
        for dep in range(map_width):
            if cos_a > 0:
                vd = in_block_pos['right'] / cos_a + block_size / cos_a * dep + 1
            elif cos_a < 0:
                vd = in_block_pos['left'] / -cos_a + block_size / -cos_a * dep + 1

            xv, yv = vd * cos_a + player.x, vd * sin_a + player.y
            fixed = (xv // block_size * block_size, yv // block_size * block_size)
            if fixed in block_map:
                founded = True
                texture_v = block_map_textures[fixed]
                break

        # Горизонтали
        for dep in range(map_height):
            if sin_a > 0:
                hd = in_block_pos['bottom'] / sin_a + block_size / sin_a * dep + 1
            elif sin_a < 0:
                hd = in_block_pos['top'] / -sin_a + block_size / -sin_a * dep + 1

            xh, yh = hd * cos_a + player.x, hd * sin_a + player.y
            fixed = (xh // block_size * block_size, yh // block_size * block_size)
            if fixed in block_map:
                founded = True
                texture_h = block_map_textures[fixed]
                break


        if founded:
            if hd > vd:
                ray_size = vd
                margin = yv
                text_num = texture_v
            else:
                ray_size = hd
                margin = xh
                text_num = texture_h
            margin = int(margin) % block_size
            ray_size *= cos(player.angle - cur_angle)
            height_c = coefficient / (ray_size + 0.0001)
            wall_line = textures[text_num].subsurface(margin * texture_scale, 0, texture_scale, texture_size)
            wall_line = pygame.transform.scale(wall_line, (scale, int(height_c)))
            display.blit(wall_line, (ray * scale, half_height - height_c // 2))