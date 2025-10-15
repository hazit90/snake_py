"""
Snake Game - Main Entry Point

A classic Snake game implemented in Python using pygame.
The game features modular code organization for easy maintenance and extension.

Author: AI Assistant
Date: October 2025
"""

from game import SnakeGame

def main():
    """Entry point for the Snake game"""
    try:
        print("Starting Snake Game...")
        print("Controls:")
        print("  - Use arrow keys or WASD to move")
        print("  - ESC to quit")
        print("  - SPACE to restart when game over")
        print("\nEnjoy the game!")
        
        game = SnakeGame()
        game.run()
        
    except ImportError as e:
        print(f"Error: Missing required dependency - {e}")
        print("Please install pygame: pip install pygame")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()