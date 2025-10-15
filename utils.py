# Game constants and utility functions

import pygame
from enum import Enum

# Game constants
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
GRID_SIZE = 20
GRID_WIDTH = WINDOW_WIDTH // GRID_SIZE
GRID_HEIGHT = WINDOW_HEIGHT // GRID_SIZE

# Colors (RGB)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
DARK_GREEN = (0, 150, 0)
BLUE = (0, 0, 255)

# Game settings
FPS = 10
INITIAL_SNAKE_LENGTH = 3

class Direction(Enum):
    """Enum for snake movement directions"""
    UP = (0, -1)
    DOWN = (0, 1)
    LEFT = (-1, 0)
    RIGHT = (1, 0)

def is_valid_position(x, y):
    """Check if position is within game boundaries"""
    return 0 <= x < GRID_WIDTH and 0 <= y < GRID_HEIGHT

def get_opposite_direction(direction):
    """Get the opposite direction to prevent snake from moving backwards"""
    opposites = {
        Direction.UP: Direction.DOWN,
        Direction.DOWN: Direction.UP,
        Direction.LEFT: Direction.RIGHT,
        Direction.RIGHT: Direction.LEFT
    }
    return opposites.get(direction)