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
Grid = namedtuple("Grid", ["dimension", "cells"])
Neighbors = namedtuple("Neighbors", ["number"])

