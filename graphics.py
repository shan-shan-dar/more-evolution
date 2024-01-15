import pygame
import parameters as param

# Constants for visualization
SCREEN_WIDTH, SCREEN_HEIGHT = 800, 800
GRID_SIZE = param.GridX, param.GridY
CELL_SIZE = SCREEN_WIDTH // GRID_SIZE[0], SCREEN_HEIGHT // GRID_SIZE[1]

# Colors
WHITE = "#ffffff"
BLACK = "#000000"


def draw_dots(screen, population):
    for dot in population.dots:
        if dot.alive:
            x, y = dot.loc
            pygame.draw.circle(
                screen,
                dot.color,
                (
                    int(x * CELL_SIZE[0] + CELL_SIZE[0] / 2),
                    int(y * CELL_SIZE[1] + CELL_SIZE[1] / 2),
                ),
                CELL_SIZE[0] // 2,
            )
