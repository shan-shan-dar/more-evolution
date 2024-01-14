from dot import Dot


class Population:
    def __init__(self, grid):
        self.dots = []
        self.grid = grid

    def fill(self, size):
        self.dots = [Dot(index, None) for index in range(size)]

        self.grid.update(self)

    def kill(self, index):
        if self.dots[index]:
            self.dots[index].alive = False

        self.grid.update(self)

    def move(self, index, newLoc):
        if self.dots[index]:
            self.dots[index].loc = newLoc

        self.grid.update(self)

    def cull(self):
        self.dots = [indiv for indiv in self.dots if indiv and indiv.alive]

        self.grid.update(self)

    def getDot(self, index):
        if self.dots[index]:
            return self.dots[index]

    def __getitem__(self, index):
        return self.dots[index]
