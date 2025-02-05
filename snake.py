import curses
import random

def setup_window():
    curses.initscr()
    win = curses.newwin(20, 60, 0, 0)  # Window size
    win.keypad(True)
    curses.noecho()
    curses.curs_set(0)
    win.border(0)
    win.timeout(100)
    return win

def main():
    win = setup_window()
    
    snake = [[10, 15], [10, 14], [10, 13]]  # Initial snake position
    food = [random.randint(1, 18), random.randint(1, 58)]
    win.addch(food[0], food[1], '*')
    
    key = curses.KEY_RIGHT  # Initial direction
    
    while True:
        next_key = win.getch()
        key = key if next_key == -1 else next_key
        
        # Update snake head position
        head = [snake[0][0], snake[0][1]]
        if key == curses.KEY_DOWN:
            head[0] += 1
        elif key == curses.KEY_UP:
            head[0] -= 1
        elif key == curses.KEY_LEFT:
            head[1] -= 1
        elif key == curses.KEY_RIGHT:
            head[1] += 1
        
        # Check for collisions
        if head in snake or head[0] == 0 or head[0] == 19 or head[1] == 0 or head[1] == 59:
            break  # Game over
        
        snake.insert(0, head)
        
        # Check if food is eaten
        if head == food:
            food = None
            while food is None:
                new_food = [random.randint(1, 18), random.randint(1, 58)]
                food = new_food if new_food not in snake else None
            win.addch(food[0], food[1], '*')
        else:
            tail = snake.pop()
            win.addch(tail[0], tail[1], ' ')
        
        # Draw snake
        win.addch(snake[0][0], snake[0][1], '#')
    
    curses.endwin()
    print("Game Over!")

if __name__ == "__main__":
    main()
