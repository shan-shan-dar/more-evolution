# simulation.py
import random
import time
import matplotlib.pyplot as plt
from grid import Grid
from population import Population


def visualize(grid, population):
    fig, ax = plt.subplots()

    # Draw the grid lines
    for i in range(grid.size_x() + 1):
        ax.axvline(x=i, color="black", linestyle="-", linewidth=0.1)
    for i in range(grid.size_y() + 1):
        ax.axhline(y=i, color="black", linestyle="-", linewidth=0.1)

    # Draw dots based on grid content
    for x in range(grid.size_x()):
        for y in range(grid.size_y()):
            value = grid.at((x, y))

            if value == grid.EMPTY:
                # Empty place
                continue
            elif value < len(population.dots) and population.dots[value].alive:
                # Dot at this location
                center_x = x + 0.5
                center_y = y + 0.5
                circle = plt.Circle(
                    (center_x, center_y),
                    0.4,
                    color=population.dots[value].color,
                    fill=True,
                )
                ax.add_patch(circle)

    ax.set_aspect("equal", adjustable="box")
    ax.set_xlim(0, grid.size_x())  # Set x-axis limits
    ax.set_ylim(0, grid.size_y())  # Set y-axis limits
    plt.axis("off")  # Turn off axis labels

    plt.show()


if __name__ == "__main__":
    grid = Grid()
    grid.init(100, 100)

    population = Population(grid)
    population.fill(100)

    for dot in population.dots:
        if dot.alive:
            # Choose a random empty location for the dot
            while True:
                random_loc = (
                    random.randint(0, grid.size_x() - 1),
                    random.randint(0, grid.size_y() - 1),
                )
                if grid.is_empty_at(random_loc):
                    break
            population.move(dot.index, random_loc)

    visualize(grid, population)
