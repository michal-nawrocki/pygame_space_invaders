class GameSettings:
    def __init__(self, width=1280, height=720):
        self.max_player_projectiles = 5
        self.min_delay_between_shots = 500
        self._screen_width = width
        self._screen_height = height

    @property
    def screen_height(self):
        return self._screen_height

    @screen_height.setter
    def screen_height(self, screen_height):
        self._screen_height = screen_height

    @property
    def screen_width(self):
        return self._screen_width

    @screen_width.setter
    def screen_width(self, screen_width):
        self._screen_width = screen_width
