import random

import pygame

from space_invaders.entities import (
    Alien,
    Player,
    Projectile,
)
from space_invaders.game.game_settings import GameSettings
from space_invaders.game.helpers.input_helpers import handle_keyboard_inputs
from space_invaders.game.helpers.setup_helpers import prepare_aliens_list
from space_invaders.game.helpers.time_helpers import has_time_passed


class GameCoordinator:
    def __init__(self):
        self.alien_move_delay = 0
        self.alien_shoot_delay = 0
        self.count_rebounds = 0
        self.current_time = 0
        self.enemies: [Alien] = []
        self.enemies_direction = -1
        self.enemies_move_down = False
        self.horizontal_delay = 0
        self.last_projectile_time = 0
        self.player_projectiles = 0
        self.projectiles: [Projectile] = []
        self.running = True
        self.settings = GameSettings()
        self.vertical_delay = 0

    def _setup_pygame(self):
        pygame.init()
        pygame.font.init()
        self.font = pygame.font.Font(None, 27)
        self.screen = pygame.display.set_mode(
            size=(self.settings.screen_width, self.settings.screen_height),
            flags=pygame.SCALED,
        )
        pygame.display.set_caption("Michal Nawrocki's Space Invaders")
        self.clock = pygame.time.Clock()

    def _prepare_game(self):
        self.player = Player(
            pos=(self.settings.screen_width * 0.5, self.settings.screen_height * 0.9)
        )

        self.enemies = prepare_aliens_list(6, 6)
        self.screen.blit(self.player.image, self.player.pos)

        for entity in self.enemies:
            self.screen.blit(entity.image, entity.pos)

    def _close(self):
        self.running = False
        print("Goodbye")

    def _handle_inputs(self):
        pygame.event.pump()
        keys_pressed = pygame.key.get_pressed()
        handle_keyboard_inputs(keys_pressed, self)

    def _update_positions(self):
        # Move all projectiles up or down
        for entity in self.projectiles:
            entity.move_vertical(self.settings)

        # Check if should update position of aliens
        if has_time_passed(
            current_time=self.current_time,
            last_time=self.alien_move_delay,
            delay=self.settings.alien_move_interval
        ):
            for entity in self.enemies:
                entity.move_in_pattern(
                    self.settings,
                    horizontal_dir=self.enemies_direction,
                    move_down=self.enemies_move_down,
                )
            self.enemies_move_down = False
            self.alien_move_delay = self.current_time

    def _play_sounds(self):
        pass

    def _do_collisions(self):
        # Handle collisions of projectiles
        for entity in self.projectiles:
            # Check if Player has been hit
            if entity.rect.colliderect(self.player.rect):
                entity.to_be_removed = True
                self.running = False
                print("I've been hit")

            # Check if it's players rocket and if it hit alien
            if not entity.is_enemy:
                for alien in self.enemies:
                    if alien.rect.colliderect(entity.rect):
                        entity.to_be_removed = True
                        alien.to_be_removed = True
                        break

            # Check if rocket should be removed
            if entity.to_be_removed:
                self.projectiles.remove(entity)

        # Remove destroyed aliens
        for entity in self.enemies:
            if entity.to_be_removed:
                self.enemies.remove(entity)

    def _handle_ai(self):
        # Check if aliens should move one level down
        if self.count_rebounds == 4:
            self.enemies_move_down = True
            self.count_rebounds = 0

        # Check if aliens should change move direction
        if has_time_passed(
            current_time=self.current_time,
            last_time=self.horizontal_delay,
            delay=self.settings.alien_change_direction_interval
        ):
            self.enemies_direction = -1 if self.enemies_direction != -1 else 1
            self.horizontal_delay = self.current_time
            self.count_rebounds += 1

        # Check if the alien should try to shoot
        if has_time_passed(
            current_time=self.current_time,
            last_time=self.alien_shoot_delay,
            delay=self.settings.alien_shot_interval
        ):
            random_index = random.randint(0, len(self.enemies) - 1)
            entity = self.enemies[random_index]
            self.projectiles.append(
                Projectile(
                    pos=(
                        entity.pos[0] + self.player.image.get_width() / 2 - 3,
                        entity.pos[1],
                    ),
                    speed_y=3,
                    speed_x=0,
                    is_enemy=True,
                )
            )
            self.alien_shoot_delay = self.current_time

    def _render(self):
        # Reset screen to black
        self.screen.fill((0, 0, 0))

        #  Draw player
        self.screen.blit(self.player.image, self.player.pos)

        # Draw enemies
        for entity in self.enemies:
            self.screen.blit(entity.image, entity.pos)

        # Draw projectiles
        for entity in self.projectiles:
            self.screen.blit(entity.image, entity.pos)

        # # Draw text
        # text = self.font.render(
        #     f"Self.enemies_move_down: {self.enemies_move_down}", True, (0, 255, 0), (0, 0, 0)
        # )
        # self.screen.blit(text, (0, 0))

        pygame.display.update()
        self.clock.tick(60)

    def start(self):
        self._setup_pygame()
        self._prepare_game()

        while self.running:
            self.current_time = pygame.time.get_ticks()
            self._handle_inputs()
            self._update_positions()
            self._handle_ai()
            self._do_collisions()
            self._render()
            self._play_sounds()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self._close()
