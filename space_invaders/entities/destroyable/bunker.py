import pygame

from space_invaders.entities.destroyable.bunker_block import BunkerBlock


class Bunker:
    def __init__(self, pos=(int, int)):
        self.bunker_blocks: [BunkerBlock] = []
        self._make_bunker(pos)

    def _make_bunker(self, pos: [int, int]):
        # 1st row
        self.bunker_blocks.append(BunkerBlock(pos))
        self.bunker_blocks.append(BunkerBlock((pos[0]+6, pos[1])))
        self.bunker_blocks.append(BunkerBlock((pos[0]+12, pos[1])))

        self.bunker_blocks.append(BunkerBlock((pos[0]+30, pos[1])))
        self.bunker_blocks.append(BunkerBlock((pos[0]+36, pos[1])))
        self.bunker_blocks.append(BunkerBlock((pos[0]+42, pos[1])))

        # 2nd row
        self.bunker_blocks.append(BunkerBlock((pos[0], pos[1]-6)))
        self.bunker_blocks.append(BunkerBlock((pos[0]+6, pos[1]-6)))
        self.bunker_blocks.append(BunkerBlock((pos[0]+12, pos[1]-6)))

        self.bunker_blocks.append(BunkerBlock((pos[0]+30, pos[1]-6)))
        self.bunker_blocks.append(BunkerBlock((pos[0]+36, pos[1]-6)))
        self.bunker_blocks.append(BunkerBlock((pos[0]+42, pos[1]-6)))

        # 3rd row
        self.bunker_blocks.append(BunkerBlock((pos[0], pos[1]-12)))
        self.bunker_blocks.append(BunkerBlock((pos[0]+6, pos[1]-12)))
        self.bunker_blocks.append(BunkerBlock((pos[0]+12, pos[1]-12)))

        self.bunker_blocks.append(BunkerBlock((pos[0]+30, pos[1]-12)))
        self.bunker_blocks.append(BunkerBlock((pos[0]+36, pos[1]-12)))
        self.bunker_blocks.append(BunkerBlock((pos[0]+42, pos[1]-12)))

        # 4th row
        self.bunker_blocks.append(BunkerBlock((pos[0], pos[1]-18)))
        self.bunker_blocks.append(BunkerBlock((pos[0]+6, pos[1]-18)))
        self.bunker_blocks.append(BunkerBlock((pos[0]+12, pos[1]-18)))
        self.bunker_blocks.append(BunkerBlock((pos[0]+18, pos[1]-18)))
        self.bunker_blocks.append(BunkerBlock((pos[0]+24, pos[1]-18)))
        self.bunker_blocks.append(BunkerBlock((pos[0]+30, pos[1]-18)))
        self.bunker_blocks.append(BunkerBlock((pos[0]+36, pos[1]-18)))
        self.bunker_blocks.append(BunkerBlock((pos[0]+42, pos[1]-18)))

        # 5th row
        self.bunker_blocks.append(BunkerBlock((pos[0]+6, pos[1]-24)))
        self.bunker_blocks.append(BunkerBlock((pos[0]+12, pos[1]-24)))
        self.bunker_blocks.append(BunkerBlock((pos[0]+18, pos[1]-24)))
        self.bunker_blocks.append(BunkerBlock((pos[0]+24, pos[1]-24)))
        self.bunker_blocks.append(BunkerBlock((pos[0]+30, pos[1]-24)))
        self.bunker_blocks.append(BunkerBlock((pos[0]+36, pos[1]-24)))

        # 6th row
        self.bunker_blocks.append(BunkerBlock((pos[0]+12, pos[1]-30)))
        self.bunker_blocks.append(BunkerBlock((pos[0]+18, pos[1]-30)))
        self.bunker_blocks.append(BunkerBlock((pos[0]+24, pos[1]-30)))
        self.bunker_blocks.append(BunkerBlock((pos[0]+30, pos[1]-30)))

        # 7th row
        self.bunker_blocks.append(BunkerBlock((pos[0]+18, pos[1]-36)))
        self.bunker_blocks.append(BunkerBlock((pos[0]+24, pos[1]-36)))

