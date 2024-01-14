from enums import Compass


class Dot:
    def __init__(self, index, loc):
        self.index = index
        self.alive = True
        self.color = "#7B7B7B"
        self.loc = loc
