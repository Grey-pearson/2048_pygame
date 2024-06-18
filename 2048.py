import sys
import time
from collections import defaultdict, namedtuple
from copy import deepcopy
import pygame
"""
create dynamic board size at begining of game (initially 4x4 tho)
a '2' tile pops up randomly every turn
choose wasd and that moves all tiles in that dirrection
if two tiles of same int collide they combine and double
"""

Dimension = namedtuple("Dimension", ["width", "height"])
Cells = namedtuple("Cells", ["x","y","number"])
Grid = namedtuple("Grid", ["dimension", "cells"])
Neighbors = namedtuple("Neighbors", ["number"]) # may not be used

# needs some trial and error to figure out how this works
STARTING_GRID = Grid(
    Dimension(4,4),
    Cells{
        (0,0,0)
    }
)

def draw_grid(screen: pygame.Surface, grid: Grid) -> None:
    cell_width = screen.get_width() / grid.dimension.width 
    cell_height = screen.get_height() / grid.dimension.width 
    border_size = 2

    # for x, y in grid.cells:
    #     pygame.draw.rect()