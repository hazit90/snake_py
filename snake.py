import pygame
from utils import Direction, GREEN, DARK_GREEN, GRID_SIZE, is_valid_position, get_opposite_direction, INITIAL_SNAKE_LENGTH

class Snake:
    """Handles snake movement, growth, and rendering"""
    
    def __init__(self, start_x, start_y):
        self.body = []
        self.direction = Direction.RIGHT
        self.grow_pending = 0
        
        # Initialize snake body
        for i in range(INITIAL_SNAKE_LENGTH):
            self.body.append((start_x - i, start_y))
    
    def get_head(self):
        """Get the position of snake's head"""
        return self.body[0] if self.body else None
    
    def move(self):
        """Move the snake in current direction"""
        if not self.body:
            return False
            
        head_x, head_y = self.body[0]
        direction_x, direction_y = self.direction.value
        new_head = (head_x + direction_x, head_y + direction_y)
        
        # Check if new head position is valid
        if not is_valid_position(new_head[0], new_head[1]):
            return False
        
        # Check if snake collides with itself
        if new_head in self.body:
            return False
        
        # Add new head
        self.body.insert(0, new_head)
        
        # Remove tail unless snake should grow
        if self.grow_pending > 0:
            self.grow_pending -= 1
        else:
            self.body.pop()
        
        return True
    
    def change_direction(self, new_direction):
        """Change snake direction if it's not opposite to current direction"""
        if new_direction != get_opposite_direction(self.direction):
            self.direction = new_direction
    
    def grow(self):
        """Mark snake to grow on next move"""
        self.grow_pending += 1
    
    def draw(self, screen):
        """Draw the snake on the screen"""
        for i, (x, y) in enumerate(self.body):
            rect = pygame.Rect(
                x * GRID_SIZE,
                y * GRID_SIZE,
                GRID_SIZE,
                GRID_SIZE
            )
            
            # Draw head differently from body
            color = GREEN if i == 0 else DARK_GREEN
            pygame.draw.rect(screen, color, rect)
            pygame.draw.rect(screen, (0, 100, 0), rect, 2)  # Dark green border
    
    def get_length(self):
        """Get current snake length"""
        return len(self.body)