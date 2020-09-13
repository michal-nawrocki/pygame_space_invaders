from pathlib import Path

import pygame

_root_path = Path().cwd().joinpath("assets/sprites/")
SPACESHIP = pygame.image.load(str(_root_path.joinpath("player/ship.png").resolve()))
ROCKET = pygame.image.load(str(_root_path.joinpath("player/rocket.png").resolve()))
BUNKER_BLOCK = pygame.image.load(str(_root_path.joinpath("bunker/bunker_block.png").resolve()))

ALIEN_A = pygame.image.load(str(_root_path.joinpath("aliens/alien_a.png").resolve()))
ALIEN_B = pygame.image.load(str(_root_path.joinpath("aliens/alien_b.png").resolve()))
ALIEN_C = pygame.image.load(str(_root_path.joinpath("aliens/alien_c.png").resolve()))
ALIEN_D = pygame.image.load(str(_root_path.joinpath("aliens/alien_d.png").resolve()))
ALIEN_E = pygame.image.load(str(_root_path.joinpath("aliens/alien_e.png").resolve()))
ALIEN_F = pygame.image.load(str(_root_path.joinpath("aliens/alien_f.png").resolve()))
