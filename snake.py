import curses
from curses import KEY_DOWN, KEY_UP, KEY_LEFT, KEY_RIGHT
from random import randint

X_MAX = 135
Y_MAX = 40
X_MIN = 7
Y_MIN = 3
MAX_LENGTH = 60

arrow = {
  KEY_RIGHT: '>', KEY_LEFT: '<', KEY_UP: '^', KEY_DOWN: 'v'
}

pos_updates = {
  KEY_RIGHT: (1, 0), KEY_LEFT: (-1, 0),
  KEY_DOWN: (0, 1), KEY_UP: (0, -1)
}

def play_snake():
  screen = curses.initscr()
  curses.resize_term(46, 150)
  curses.curs_set(0)
  curses.noecho()
  screen.clear()
  game_win, score_win = set_up_windows()
  current_direction = active_key = KEY_RIGHT
  update_pos = lambda cur_x, cur_y, update: (cur_x+update[0], cur_y+update[1])
  x, y, escape = 65, 20, 27
  snake, food, score = [(y, x)], (randint(Y_MIN+3, Y_MAX-3), randint(X_MIN+5, X_MAX-5)), 0
  game_win.addstr(snake[-1][0], snake[-1][1], arrow[current_direction])
  game_win.addstr(food[0], food[1], '*')
  score_win.addstr(1, 1, f'SCORE: {score}')
  score_win.refresh()
  while active_key != escape:
    current_direction = active_key if active_key in pos_updates.keys() else current_direction
    x, y = update_pos(x, y, pos_updates[current_direction])
    snake.append((y, x))
    game_win.addstr(snake[-1][0], snake[-1][1], arrow[current_direction])
    game_win.refresh()
    game_win.addch(snake[0][0], snake[0][1], ' ')
    if snake[-1] == food:
      food = (randint(Y_MIN+3, Y_MAX-3), randint(X_MIN+5, X_MAX-5))
      game_win.addstr(food[0], food[1], '*')
      score += 100
      score_win.addstr(1, 1, f'SCORE: {score}')
      score_win.refresh()
    elif snake[-1] != food or len(snake) > MAX_LENGTH:
      snake.pop(0)
    x, y = check_boundaries(x, y, current_direction)
    active_key = game_win.getch()
    curses.napms(100)


def set_up_windows():
  game_win = curses.newwin(Y_MAX, X_MAX, Y_MIN-1, X_MIN-1)
  score_win = curses.newwin(3, 10, 42, 65)
  game_win.box()
  game_win.keypad(True)
  game_win.refresh()
  game_win.timeout(00)
  return game_win, score_win


def check_boundaries(x, y, current_direction):
  new_x = 2 if ((x > X_MAX-3 and current_direction==KEY_RIGHT) or x==X_MAX-2) else x
  new_x = X_MAX-2 if ((x < 2 and current_direction==KEY_LEFT) or x==1) else new_x
  new_y = 2 if ((y>Y_MAX-3 and current_direction==KEY_UP) or y==Y_MAX-2) else y
  new_y = Y_MAX-2 if ((y<1 and current_direction==KEY_UP) or y==1) else new_y
  return new_x, new_y


if __name__=='__main__':
  play_snake()