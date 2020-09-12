from pygame import sprite

from space_invaders.entities import assets_loader
from space_invaders.entities import Alien

ALIEN_SPRITE_LIST = [
    assets_loader.ALIEN_F,
    assets_loader.ALIEN_E,
    assets_loader.ALIEN_D,
    assets_loader.ALIEN_C,
    assets_loader.ALIEN_B,
    assets_loader.ALIEN_A,
]


def _get_alien_sprite(row) -> sprite:
    index = row % len(ALIEN_SPRITE_LIST)
    return ALIEN_SPRITE_LIST[index]


def prepare_aliens_list(rows: int, cols: int) -> [Alien]:
    alien_list = []
    cord_gap = 50
    x_start = 400
    y_cord = 100

    for row in range(0, rows):
        x_cord = x_start
        for _ in range(0, cols):
            alien = Alien(pos=(x_cord, y_cord), alien_sprite=_get_alien_sprite(row))
            alien_list.insert(0, alien)

            x_cord += cord_gap

        y_cord += cord_gap

    return alien_list
