# Snake Terminal Game

A classic Snake game implementation that runs in the terminal, built with Python and the curses library.

## Features
- Control the snake using arrow keys
- Eat food ($) to grow and increase score
- Avoid hitting walls (#) or yourself
- Score tracking based on food consumed
- Game over screen with final score display

## Requirements
- Python 3.x
- curses library (comes built-in with Python on Unix-like systems)
- Windows users may need to install `windows-curses` via pip:
```bash
pip install windows-curses
```

## How to Play
1. Clone the repository:
```bash
git clone https://github.com/makalin/Snake-Terminal.git
cd Snake-Terminal
```

2. Run the game:
```bash
python snake.py
```

3. Controls:
- Arrow Keys: Move the snake up, down, left, or right
- Q: Quit the game at any time

## Gameplay
- The snake is represented by 'O' (head) and 'o' (body)
- Food is shown as '$'
- Walls are represented by '#'
- Eat food to grow longer and increase your score
- Game ends if you hit a wall or the snake's own body

## Code Structure
- Uses Python's curses library for terminal interface
- Main game loop handles input, movement, and collision detection
- Random food spawning system
- Score tracking and display

## Example Gameplay
```
Score: 2
####################
#                  #
#    Oooo$         #
#                  #
#                  #
####################
```

## Contributing
Feel free to fork the repository and submit pull requests with improvements such as:
- High score tracking
- Speed increase with score
- Different food types
- Color support

## License
This project is open-source and available under the MIT License.
