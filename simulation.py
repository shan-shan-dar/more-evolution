# simulation.py
import random
import time

import pygame
import sys

from grid import Grid
from population import Population
import parameters as param
import graphics as gfx

# Pygame setup
pygame.init()
clock = pygame.time.Clock()

# Pygame screen setup
screen = pygame.display.set_mode((gfx.SCREEN_WIDTH, gfx.SCREEN_HEIGHT))
pygame.display.set_caption("Simulation")

if __name__ == "__main__":
    # initializing stuff
    grid = Grid()
    grid.init(param.GridX, param.GridY)

    population = Population(grid)
    population.fill(param.Gen0Population)

    generationCount = 0

    grid.initGen0(population)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        for generation in range(param.MaxGenerations):
            for simStep in range(param.StepsPerGeneration):
                for dot in population.dots:
                    # Logic for each dot
                    new_loc = (
                        dot.loc[0] + random.randint(-1, 1),
                        dot.loc[1] + random.randint(-1, 1),
                    )
                    if grid.is_in_bounds(new_loc) and grid.is_empty_at(new_loc):
                        population.move(dot.index, new_loc)

                # Logic for each simStep

                # Visualization
                screen.fill(gfx.BLACK)
                gfx.draw_dots(screen, population)

                pygame.display.flip()
                clock.tick(10)

            # Logic for each generation
            generationCount += 1
        break
