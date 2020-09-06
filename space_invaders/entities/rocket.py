import pygame

from space_invaders.entities import Entity
from space_invaders.entities import assets_loader


class Projectile(Entity):
    def __init__(self, pos: (int, int), speed_x, speed_y, is_enemy=False):
        self.is_enemy = is_enemy
        image = assets_loader.ROCKET

        if is_enemy:
            image = pygame.transform.flip(image, False, True)

        super().__init__(
            pos,
            image,
            x_speed=speed_x,
            y_speed=speed_y,
        )
