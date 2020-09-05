from typing import Tuple

from space_invaders.entities import Entity
from space_invaders.entities import assets_loader


class Player(Entity):
    def __init__(self, pos: Tuple[int, int]):
        super().__init__(assets_loader.SPACESHIP, pos, health=100)

