from pygame.sprite import Sprite
from pygame.surface import Surface


class Entity(Sprite):
    def __init__(
        self,
        pos: (int, int),
        sprite: Surface,
        health: int = 0,
        x_speed: int = 0,
        y_speed: int = 0,

    ):
        super().__init__()
        self.image = sprite
        self._pos = pos
        self._dx = x_speed
        self._dy = y_speed
        self.rect = self.image.get_rect(center=pos)
        self.health = health
        self.to_be_removed = False

    def move_left(self, settings):
        self.pos = (self.pos[0]-self._dx, self.pos[1])
        if self.pos[0] < 0:
            self.pos = (0, self.pos[1])

        self.rect.center = self.pos

    def move_right(self, settings):
        self.pos = (self.pos[0]+self._dx, self.pos[1])
        if self.pos[0] > settings.screen_width - self.image.get_width():
            self.pos = (settings.screen_width - self.image.get_width(), self.pos[1])

        self.rect.center = self.pos

    def move_vertical(self, settings):
        self.pos = (self.pos[0], self.pos[1] + self._dy)

        if self.pos[1] > settings.screen_height - self.image.get_height():
            self.pos = (self.pos[0], settings.screen_height - self.image.get_height())
            self.to_be_removed = True

        elif self.pos[1] < 0:
            self.pos = (self.pos[0], 0)
            self.to_be_removed = True

        self.rect.center = self.pos

    @property
    def pos(self):
        return self._pos

    @pos.setter
    def pos(self, pos):
        self._pos = pos
