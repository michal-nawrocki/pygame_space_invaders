class GameSettings:
    def __init__(self, width=1024, height=576):
        self._alien_move_delay_interval = 300
        self._alien_shoot_delay_interval = 1000
        self._alien_change_dir_interval = 6000
        self._player_shots_delay = 500
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

    @property
    def alien_change_direction_interval(self):
        return self._alien_change_dir_interval

    @alien_change_direction_interval.setter
    def alien_change_direction_interval(self, interval):
        self._alien_change_dir_interval = interval

    @property
    def alien_move_interval(self):
        return self._alien_move_delay_interval

    @alien_move_interval.setter
    def alien_move_interval(self, interval):
        self._alien_move_delay_interval = interval

    @property
    def alien_shot_interval(self):
        return self._alien_shoot_delay_interval

    @alien_shot_interval.setter
    def alien_shot_interval(self, interval):
        self.alien_shot_interval = interval

    @property
    def player_shot_interval(self):
        return self._player_shots_delay

    @player_shot_interval.setter
    def player_shot_interval(self, interval):
        self._player_shots_delay = interval
