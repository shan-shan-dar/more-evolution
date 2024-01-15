from enums import Compass
import random


class Dot:
    def __init__(self, index, loc):
        self.index = index
        self.alive = True
        self.color = "#{:06x}".format(random.randint(0x101010, 0xFFFFFF))
        self.loc = loc
