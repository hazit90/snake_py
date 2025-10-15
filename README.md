# Snake Game 🐍

A classic Snake game implemented in Python using pygame with modular, readable code architecture.

## Features

- **Modular Design**: Well-organized code split into logical modules
- **Smooth Gameplay**: 60 FPS game loop with responsive controls
- **Score Tracking**: Real-time score and snake length display
- **Game Over Screen**: Clear game over indication with restart option
- **Flexible Controls**: Support for both arrow keys and WASD
- **Collision Detection**: Proper boundary and self-collision detection
- **Food Generation**: Smart food placement avoiding snake body

## Project Structure

```
snake_py/
├── main.py          # Entry point and game launcher
├── game.py          # Main game class and game loop
├── snake.py         # Snake logic and movement
├── food.py          # Food generation and management
├── utils.py         # Constants and utility functions
├── requirements.txt # Python dependencies
└── README.md        # This file
```

## Installation

1. **Clone or download the project**
2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```
   Or install pygame directly:
   ```bash
   pip install pygame
   ```

## How to Run

```bash
python main.py
```

## Controls

- **Movement**: Arrow keys or WASD
- **Quit**: ESC key
- **Restart** (when game over): SPACE key

## Game Rules

1. Control the green snake to eat red food
2. Each food eaten increases your score by 10 points
3. The snake grows longer after eating food
4. Avoid hitting the walls or the snake's own body
5. Try to achieve the highest score possible!

## Code Architecture

### `utils.py`
Contains all game constants, color definitions, and utility functions:
- Game dimensions and grid settings
- Color constants for consistent theming
- Direction enumeration for clean movement logic
- Helper functions for position validation

### `snake.py`
Handles all snake-related functionality:
- Snake movement and direction changes
- Growth mechanics
- Collision detection (self and boundaries)
- Rendering with distinct head/body colors

### `food.py`
Manages food generation and interaction:
- Random food placement
- Collision detection with snake
- Smart positioning to avoid snake body
- Visual rendering with border effects

### `game.py`
Main game controller:
- Game state management
- Event handling (keyboard input)
- Game loop coordination
- Score tracking and display
- Game over logic and restart functionality

### `main.py`
Application entry point:
- Error handling for missing dependencies
- User-friendly startup messages
- Clean separation of game logic from execution

## Customization

The modular design makes it easy to customize:

- **Game Speed**: Modify `FPS` in `utils.py`
- **Colors**: Update color constants in `utils.py`
- **Grid Size**: Change `GRID_SIZE` for different game feel
- **Snake Length**: Adjust `INITIAL_SNAKE_LENGTH`
- **Scoring**: Modify score increment in `game.py`

## Dependencies

- **Python 3.6+**
- **pygame 2.0.0+**

## Future Enhancements

Potential features to add:
- High score persistence
- Multiple difficulty levels
- Sound effects and background music
- Power-ups and special food types
- Multiplayer support
- Custom themes and skins

## License

This project is open source and available under the MIT License.