import pygame

from space_invaders.entities import Player, Projectile
from space_invaders.game.game_settings import GameSettings


class GameCoordinator:
    def __init__(self):
        self.player_projectiles = 0
        self.last_projectile_time = 0
        self.settings = GameSettings()
        self.projectiles: [Projectile] = []
        self.enemies = []
        self.running = True

    def _setup_pygame(self):
        pygame.init()
        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height)
        )
        self.clock = pygame.time.Clock()

    def _prepare_game(self):
        self.player = Player(pos=(self.settings.screen_width*0.5, self.settings.screen_height*0.9))
        self.screen.blit(self.player.image, self.player.pos)

    def _close(self):
        self.running = False
        print("Goodbye")

    def _handle_inputs(self):
        pygame.event.pump()
        keys_pressed = pygame.key.get_pressed()

        if keys_pressed[pygame.K_a] or keys_pressed[pygame.K_LEFT]:
            print("holding a")
            self.player.move_left(self.settings)

        if keys_pressed[pygame.K_d] or keys_pressed[pygame.K_RIGHT]:
            print("holding d")
            self.player.move_right(self.settings)

        if keys_pressed[pygame.K_SPACE]:
            current_time = pygame.time.get_ticks()
            if self.last_projectile_time == 0 or current_time - self.last_projectile_time >= self.settings.min_delay_between_shots:
                self.projectiles.append(Projectile(pos=(self.player.pos[0] + self.player.image.get_width()/2 - 3, self.player.pos[1]), speed_y=-5, speed_x=0))
                self.last_projectile_time = current_time

        if keys_pressed[pygame.K_HOME]:
            current_time = pygame.time.get_ticks()
            if self.last_projectile_time == 0 or current_time - self.last_projectile_time >= self.settings.min_delay_between_shots:
                self.projectiles.append(Projectile(pos=(self.player.pos[0] + self.player.image.get_width()/2 - 3, 0), speed_y=10, speed_x=0, is_enemy=True))
                self.last_projectile_time = current_time

    def _update_positions(self):
        # Move all projectiles up or down
        for entity in self.projectiles:
            entity.move_vertical(self.settings)

    def _play_sounds(self):
        pass

    def _do_collisions(self):
        for entity in self.projectiles:
            if entity.to_be_removed:
                self.projectiles.remove(entity)

            if entity.rect.colliderect(self.player.rect):
                print("I've been hit")

    def _render(self):
        self.screen.fill((0, 0, 0))

        #  Draw player
        self.screen.blit(self.player.image, self.player.pos)

        # Draw projectiles
        for entity in self.projectiles:
            self.screen.blit(entity.image, entity.pos)

        pygame.display.update()
        self.clock.tick(60)

    def start(self):
        self._setup_pygame()
        self._prepare_game()

        while self.running:
            self._handle_inputs()
            self._update_positions()
            self._do_collisions()
            self._render()
            self._play_sounds()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self._close()
