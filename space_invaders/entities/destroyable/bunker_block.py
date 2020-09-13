import pygame

from space_invaders.entities import Entity


class BunkerBlock(Entity):
    def __init__(self, pos: (int, int),):
        super().__init__(pos, None)
