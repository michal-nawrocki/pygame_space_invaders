import pygame

from space_invaders.game.game_settings import GameSettings


class GameCoordinator:
    def __init__(self):
        self.settings = GameSettings()
        self.running = True

    def _setup_pygame(self):
        pygame.init()
        pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height)
        )
        self.clock = pygame.time.Clock()

    def _load_assets(self):
        pass

    def _close(self):
        self.running = False
        print("Goodbye")

    def _handle_inputs(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self._close()

    def _update_positions(self):
        pass

    def _play_sounds(self):
        pass

    def _render(self):
        self.clock.tick(60)

    def start(self):
        self._setup_pygame()
        self._load_assets()

        while self.running:
            self._handle_inputs()
            self._update_positions()
            self._play_sounds()
            self._render()
