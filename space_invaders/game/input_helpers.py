import pygame

from space_invaders.entities import Projectile


def handle_keyboard_inputs(keys_pressed, game_instance):
    current_time = pygame.time.get_ticks()

    if keys_pressed[pygame.K_a] or keys_pressed[pygame.K_LEFT]:
        game_instance.player.move_left(game_instance.settings)

    if keys_pressed[pygame.K_d] or keys_pressed[pygame.K_RIGHT]:
        game_instance.player.move_right(game_instance.settings)

    if keys_pressed[pygame.K_SPACE]:
        if (
            game_instance.last_projectile_time == 0
            or current_time - game_instance.last_projectile_time
            >= game_instance.settings.min_delay_between_shots
        ):
            game_instance.projectiles.append(
                Projectile(
                    pos=(
                        game_instance.player.pos[0]
                        + game_instance.player.image.get_width() / 2
                        - 3,
                        game_instance.player.pos[1] - 20,
                    ),
                    speed_y=-5,
                    speed_x=0,
                )
            )
            game_instance.last_projectile_time = current_time

    if keys_pressed[pygame.K_HOME]:
        if (
            game_instance.last_projectile_time == 0
            or current_time - game_instance.last_projectile_time
            >= game_instance.settings.min_delay_between_shots
        ):
            game_instance.projectiles.append(
                Projectile(
                    pos=(
                        game_instance.player.pos[0]
                        + game_instance.player.image.get_width() / 2
                        - 3,
                        0,
                    ),
                    speed_y=10,
                    speed_x=0,
                    is_enemy=True,
                )
            )
            game_instance.last_projectile_time = current_time
