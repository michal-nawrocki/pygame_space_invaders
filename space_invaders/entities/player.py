from space_invaders.entities import Entity
from space_invaders.entities import assets_loader


class Player(Entity):
    def __init__(self, pos: (int, int)):
        super().__init__(
            sprite=assets_loader.SPACESHIP,
            pos=pos,
            health=100,
            x_speed=4,
            y_speed=4,
        )

    def shoot_laser(self):
        pass
