from space_invaders.entities import assets_loader
from space_invaders.entities import Alien

ALIEN_SPRITE_LIST = [
    assets_loader.ALIEN_A,
    assets_loader.ALIEN_B,
    assets_loader.ALIEN_C,
    assets_loader.ALIEN_D,
    assets_loader.ALIEN_E,
    assets_loader.ALIEN_F,
]


def _get_alien_sprite(row):
    return ALIEN_SPRITE_LIST[len(ALIEN_SPRITE_LIST) % row]


def prepare_aliens_list(rows, columns):
    alien_list = []
    cord_gap = 50
    x_start = 400
    y_cord = 300

    for row in rows:
        x_cord = x_start
        for _ in columns:
            alien = Alien(
                pos=(x_cord, y_cord),
                alien_sprite=_get_alien_sprite(row)
            )
            alien_list.append(alien)

            x_cord += horizontal_distance

