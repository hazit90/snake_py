import pygame
import sys
from snake import Snake
from food import Food
from utils import (
    WINDOW_WIDTH, WINDOW_HEIGHT, BLACK, WHITE, BLUE,
    Direction, FPS, GRID_WIDTH, GRID_HEIGHT
)

class SnakeGame:
    """Main game class that handles game logic and rendering"""
    
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        pygame.display.set_caption("Snake Game")
        self.clock = pygame.time.Clock()
        self.font = pygame.font.Font(None, 36)
        
        # Initialize game objects
        self.reset_game()
    
    def reset_game(self):
        """Reset game to initial state"""
        start_x = GRID_WIDTH // 2
        start_y = GRID_HEIGHT // 2
        self.snake = Snake(start_x, start_y)
        self.food = Food()
        self.food.generate_position(self.snake.body)
        self.score = 0
        self.game_over = False
    
    def handle_events(self):
        """Handle pygame events"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            
            elif event.type == pygame.KEYDOWN:
                if self.game_over:
                    if event.key == pygame.K_SPACE:
                        self.reset_game()
                    elif event.key == pygame.K_ESCAPE:
                        return False
                else:
                    # Handle snake movement
                    if event.key == pygame.K_UP or event.key == pygame.K_w:
                        self.snake.change_direction(Direction.UP)
                    elif event.key == pygame.K_DOWN or event.key == pygame.K_s:
                        self.snake.change_direction(Direction.DOWN)
                    elif event.key == pygame.K_LEFT or event.key == pygame.K_a:
                        self.snake.change_direction(Direction.LEFT)
                    elif event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                        self.snake.change_direction(Direction.RIGHT)
                    elif event.key == pygame.K_ESCAPE:
                        return False
        
        return True
    
    def update_game(self):
        """Update game state"""
        if self.game_over:
            return
        
        # Move snake
        if not self.snake.move():
            self.game_over = True
            return
        
        # Check if snake ate food
        if self.food.is_eaten_by(self.snake.get_head()):
            self.snake.grow()
            self.score += 10
            self.food.generate_position(self.snake.body)
    
    def draw_text(self, text, x, y, color=WHITE):
        """Draw text on screen"""
        text_surface = self.font.render(text, True, color)
        self.screen.blit(text_surface, (x, y))
    
    def draw_game(self):
        """Render the game"""
        # Clear screen
        self.screen.fill(BLACK)
        
        if not self.game_over:
            # Draw game objects
            self.snake.draw(self.screen)
            self.food.draw(self.screen)
            
            # Draw score
            self.draw_text(f"Score: {self.score}", 10, 10)
            self.draw_text(f"Length: {self.snake.get_length()}", 10, 50)
        else:
            # Draw game over screen
            self.draw_text("GAME OVER", WINDOW_WIDTH//2 - 80, WINDOW_HEIGHT//2 - 60, color=BLUE)
            self.draw_text(f"Final Score: {self.score}", WINDOW_WIDTH//2 - 100, WINDOW_HEIGHT//2 - 20)
            self.draw_text(f"Snake Length: {self.snake.get_length()}", WINDOW_WIDTH//2 - 110, WINDOW_HEIGHT//2 + 20)
            self.draw_text("Press SPACE to play again", WINDOW_WIDTH//2 - 140, WINDOW_HEIGHT//2 + 60)
            self.draw_text("Press ESC to quit", WINDOW_WIDTH//2 - 100, WINDOW_HEIGHT//2 + 100)
        
        # Draw controls (always visible)
        self.draw_text("Controls: Arrow keys or WASD", 10, WINDOW_HEIGHT - 70)
        self.draw_text("ESC: Quit", 10, WINDOW_HEIGHT - 40)
        
        pygame.display.flip()
    
    def run(self):
        """Main game loop"""
        running = True
        
        while running:
            running = self.handle_events()
            self.update_game()
            self.draw_game()
            self.clock.tick(FPS)
        
        pygame.quit()
        sys.exit()

if __name__ == "__main__":
    game = SnakeGame()
    game.run()