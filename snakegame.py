import random
import curses

# Initialize screen
s = curses.initscr()
curses.curs_set(0)
sh, sw = s.getmaxyx()
w = curses.newwin(sh, sw, 0, 0)
w.keypad(1)
w.timeout(75)




# Initial position of the snake
snk_x = sw // 4
snk_y = sh // 2
snake = [
    [snk_y, snk_x],
    [snk_y, snk_x - 1],
    [snk_y, snk_x - 2]
]

# Initial food position
food = [sh // 2, sw // 2]
w.addch(food[0], food[1], curses.ACS_PI)

# Initial movement direction
key = curses.KEY_RIGHT

# Game loop
while True:
    next_key = w.getch()
    key = key if next_key == -1 else next_key

    # Check for collisions
    if (
        snake[0][0] in [0, sh] or
        snake[0][1] in [0, sw] or
        snake[0] in snake[1:]
    ):
        curses.endwin()
        quit()

    # Calculate new head position
    new_head = [snake[0][0], snake[0][1]]

    if key == curses.KEY_DOWN:
        new_head[0] += 1
    if key == curses.KEY_UP:
        new_head[0] -= 1
    if key == curses.KEY_LEFT:
        new_head[1] -= 1
    if key == curses.KEY_RIGHT:
        new_head[1] += 1

    snake.insert(0, new_head)

    # Check if food is eaten
    if snake[0] == food:
        food = None
        while food is None:
            nf = [
                random.randint(1, sh - 2),
                random.randint(1, sw - 2)
            ]
            if nf not in snake:
                food = nf
        w.addch(food[0], food[1], curses.ACS_PI)
    else:
        tail = snake.pop()
        w.addch(tail[0], tail[1], ' ')

    # Draw new head
    w.addch(snake[0][0], snake[0][1], curses.ACS_CKBOARD)

