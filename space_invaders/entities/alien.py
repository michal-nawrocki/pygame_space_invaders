from pygame import sprite

from space_invaders.entities import Entity


class Alien(Entity):
    def __init__(
            self,
            pos: (int, int),
            alien_sprite: sprite,
            score: int
    ):
        super().__init__(
            pos,
            alien_sprite,
            x_speed=10,
            y_speed=10,
        )
        self.rect.inflate_ip(15, 5)
        self.score = score

    def move_in_pattern(self, settings, horizontal_dir, move_down):
        if move_down:
            self.move_vertical(settings)
        else:
            if horizontal_dir == -1:
                self.move_left(settings)
            elif horizontal_dir == 1:
                self.move_right(settings)
