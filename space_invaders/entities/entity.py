from typing import Tuple

from pygame.sprite import Sprite
from pygame.surface import Surface


class Entity(Sprite):
    def __init__(
        self,
        sprite: Surface,
        pos: Tuple[int, int],
        health: int,
    ):
        super().__init__()
        self.image = sprite
        self._pos = pos
        self.rect = self.image.get_rect(center=(0, 0))
        self.health = health

    @property
    def pos(self):
        return self._pos

    @pos.setter
    def pos(self, pos):
        self._pos = pos
