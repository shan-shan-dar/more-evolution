class Grid:
    EMPTY = -1

    def __init__(self):
        self.data = []

    def init(self, size_x, size_y):
        self.data = [[0] * size_y for _ in range(size_x)]
        for column in self.data:
            for i in range(len(column)):
                column[i] = self.EMPTY

    def size_x(self):
        return len(self.data)

    def size_y(self):
        return len(self.data[0])

    def is_in_bounds(self, loc):
        return 0 <= loc[0] < self.size_x() and 0 <= loc[1] < self.size_y()

    def is_empty_at(self, loc):
        f = self.at(loc) == self.EMPTY
        return f

    def is_border(self, loc):
        return (
            loc[0] == 0
            or loc[0] == self.size_x() - 1
            or loc[1] == 0
            or loc[1] == self.size_y() - 1
        )

    def at(self, loc):
        l = self.data[loc[0]][loc[1]]
        return l

    def set(self, loc, val):
        self.data[loc[0]][loc[1]] = val

    def visit_neighborhood(self, loc, radius, func):
        center_x, center_y = loc
        for x in range(int(center_x - radius), int(center_x + radius) + 1):
            for y in range(int(center_y - radius), int(center_y + radius) + 1):
                distance = ((center_x - x) ** 2 + (center_y - y) ** 2) ** 0.5
                if distance <= radius and self.is_in_bounds((x, y)):
                    func((x, y))

    def update(self, population):
        for dot in population.dots:
            if dot.alive and dot.loc:
                self.data[dot.loc[0]][dot.loc[1]] = dot.index
