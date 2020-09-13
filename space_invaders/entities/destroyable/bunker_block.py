import pygame

from space_invaders.entities import (
    assets_loader,
    Entity
)


class BunkerBlock(Entity):
    def __init__(self, pos: (int, int),):
        super().__init__(pos, assets_loader.BUNKER_BLOCK)
        self.image = pygame.transform.scale(self.image, (6, 6))
        self.rect.inflate_ip(6, 6)
