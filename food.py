import pygame
import random
from utils import GRID_WIDTH, GRID_HEIGHT, GRID_SIZE, RED

class Food:
    """Handles food generation and rendering"""
    
    def __init__(self):
        self.position = self.generate_position()
        
    def generate_position(self, snake_body=None):
        """Generate a random position for food, avoiding snake body"""
        while True:
            x = random.randint(0, GRID_WIDTH - 1)
            y = random.randint(0, GRID_HEIGHT - 1)
            
            # If snake body is provided, ensure food doesn't spawn on snake
            if snake_body is None or (x, y) not in snake_body:
                self.position = (x, y)
                return self.position
    
    def draw(self, screen):
        """Draw the food on the screen"""
        x, y = self.position
        rect = pygame.Rect(
            x * GRID_SIZE,
            y * GRID_SIZE,
            GRID_SIZE,
            GRID_SIZE
        )
        pygame.draw.rect(screen, RED, rect)
        pygame.draw.rect(screen, (150, 0, 0), rect, 2)  # Dark red border
    
    def is_eaten_by(self, snake_head):
        """Check if food is eaten by snake"""
        return self.position == snake_head