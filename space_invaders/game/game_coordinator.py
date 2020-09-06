import random

import pygame

from space_invaders.entities import (
    Alien,
    Player,
    Projectile,
)
from space_invaders.game.game_settings import GameSettings


class GameCoordinator:
    def __init__(self):
        self.player_projectiles = 0
        self.last_projectile_time = 0
        self.horizontal_delay = 0
        self.vertical_delay = 0
        self.alien_move_delay = 0
        self.alien_shoot_delay = 0
        self.count_rebounds = 0
        self.enemies_direction = -1
        self.enemies_move_down = False
        self.settings = GameSettings()
        self.projectiles: [Projectile] = []
        self.enemies: [Alien] = []
        self.running = True

    def _setup_pygame(self):
        pygame.init()
        pygame.font.init()
        self.font = pygame.font.Font(None, 27)
        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height)
        )
        self.clock = pygame.time.Clock()

    def _prepare_game(self):
        self.player = Player(pos=(self.settings.screen_width*0.5, self.settings.screen_height*0.9))

        self.enemies.append(Alien(pos=(400, 300)))
        self.enemies.append(Alien(pos=(450, 300)))
        self.enemies.append(Alien(pos=(500, 300)))
        self.enemies.append(Alien(pos=(550, 300)))
        self.enemies.append(Alien(pos=(600, 300)))
        self.enemies.append(Alien(pos=(650, 300)))

        self.enemies.append(Alien(pos=(400, 350)))
        self.enemies.append(Alien(pos=(450, 350)))
        self.enemies.append(Alien(pos=(500, 350)))
        self.enemies.append(Alien(pos=(550, 350)))
        self.enemies.append(Alien(pos=(600, 350)))
        self.enemies.append(Alien(pos=(650, 350)))

        self.screen.blit(self.player.image, self.player.pos)

        for entity in self.enemies:
            self.screen.blit(entity.image, entity.pos)

    def _close(self):
        self.running = False
        print("Goodbye")

    def _handle_inputs(self):
        pygame.event.pump()
        keys_pressed = pygame.key.get_pressed()

        if keys_pressed[pygame.K_a] or keys_pressed[pygame.K_LEFT]:
            self.player.move_left(self.settings)

        if keys_pressed[pygame.K_d] or keys_pressed[pygame.K_RIGHT]:
            self.player.move_right(self.settings)

        if keys_pressed[pygame.K_SPACE]:
            current_time = pygame.time.get_ticks()
            if self.last_projectile_time == 0 or current_time - self.last_projectile_time >= self.settings.min_delay_between_shots:
                self.projectiles.append(Projectile(pos=(self.player.pos[0] + self.player.image.get_width()/2 - 3, self.player.pos[1] - 20), speed_y=-5, speed_x=0))
                self.last_projectile_time = current_time

        if keys_pressed[pygame.K_HOME]:
            current_time = pygame.time.get_ticks()
            if self.last_projectile_time == 0 or current_time - self.last_projectile_time >= self.settings.min_delay_between_shots:
                self.projectiles.append(Projectile(pos=(self.player.pos[0] + self.player.image.get_width()/2 - 3, 0), speed_y=10, speed_x=0, is_enemy=True))
                self.last_projectile_time = current_time

    def _update_positions(self):
        current_time = pygame.time.get_ticks()
        # Move all projectiles up or down
        for entity in self.projectiles:
            entity.move_vertical(self.settings)

        if self.alien_move_delay == 0 or current_time - self.alien_move_delay >= 300:
            for entity in self.enemies:
                entity.move_in_pattern(
                    self.settings,
                    horizontal_dir=self.enemies_direction,
                    move_down=self.enemies_move_down
                )
            self.enemies_move_down = False
            self.alien_move_delay = current_time

        if self.alien_shoot_delay == 0 or current_time - self.alien_shoot_delay >= 1000:
            entity = self.enemies[random.randint(0, len(self.enemies)-1)]
            self.projectiles.append(
                Projectile(pos=(entity.pos[0] + self.player.image.get_width() / 2 - 3, entity.pos[1]), speed_y=3,
                           speed_x=0, is_enemy=True))
            self.alien_shoot_delay = current_time

    def _play_sounds(self):
        pass

    def _do_collisions(self):
        # Handle collisions of projectiles
        for entity in self.projectiles:
            if entity.rect.colliderect(self.player.rect):
                entity.to_be_removed = True
                self.running = False
                print("I've been hit")

            for alien in self.enemies:
                if not entity.is_enemy and alien.rect.colliderect(entity.rect):
                    entity.to_be_removed = True
                    alien.to_be_removed = True

            if entity.to_be_removed:
                self.projectiles.remove(entity)

        # Remove destroyed aliens
        for entity in self.enemies:
            if entity.to_be_removed:
                self.enemies.remove(entity)

    def _handle_ai(self):
        current_time = pygame.time.get_ticks()

        if self.count_rebounds == 4:
            self.enemies_move_down = True
            self.count_rebounds = 0

        if self.horizontal_delay == 0 or current_time - self.horizontal_delay >= 4000:
            self.enemies_direction = -1 if self.enemies_direction != -1 else 1
            self.horizontal_delay = current_time
            self.count_rebounds += 1

    def _render(self):
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
            self._handle_inputs()
            self._update_positions()
            self._handle_ai()
            self._do_collisions()
            self._render()
            self._play_sounds()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self._close()
