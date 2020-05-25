import curses
from curses import KEY_DOWN, KEY_UP, KEY_LEFT, KEY_RIGHT

X_MAX = 135
Y_MAX = 40
X_MIN = 7
Y_MIN = 3


def play_snake():

  screen = curses.initscr()
  curses.noecho()
  screen.clear()
  curses.resize_term(46, 150)
  game_win = curses.newwin(Y_MAX, X_MAX, Y_MIN-1, X_MIN-1)
  game_win.box()
  game_win.keypad(True)
  game_win.refresh()
  game_win.timeout(00)
  current_direction = active_key = KEY_RIGHT
  pos_updates = {
    KEY_RIGHT: (1, 0), KEY_LEFT: (-1, 0),
    KEY_DOWN: (0, 1), KEY_UP: (0, -1)
  }
  update_pos = lambda cur_x, cur_y, update: (cur_x+update[0], cur_y+update[1])
  snake = ['>']
  x, y, escape = 65, 20, 27
  game_win.addstr( y, x, snake[-1])
  count = 0
  game_win.addstr(y, x - count, '>')
  while active_key != escape:
    count += 1
    game_win.addstr(35, 125, str((x, y)))
    current_direction = active_key if active_key in pos_updates.keys() else current_direction
    x, y = update_pos(x, y, pos_updates[current_direction])
    game_win.addstr(y, x, snake[-1])
    x, y = check_boundaries(x, y, current_direction)
    game_win.refresh()
    active_key = game_win.getch()
    curses.napms(100)


def check_boundaries(x, y, current_direction):
  new_x = 2 if ((x > X_MAX-3 and current_direction==KEY_RIGHT) or x==X_MAX-2) else x
  new_x = X_MAX-2 if ((x < 2 and current_direction==KEY_LEFT) or x==1) else new_x
  new_y = 2 if ((y>Y_MAX-3 and current_direction==KEY_UP) or y==Y_MAX-2) else y
  new_y = Y_MAX-2 if ((y<1 and current_direction==KEY_UP) or y==1) else new_y
  return new_x, new_y


if __name__=='__main__':
  play_snake()