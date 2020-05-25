import curses
from curses import KEY_DOWN, KEY_UP, KEY_LEFT, KEY_RIGHT

HEIGHT = 30
WIDTH = 50
X_MAX = HEIGHT - 2
Y_MAX = WIDTH - 2

def play_snake():

  screen = curses.initscr()

  curses.noecho()
  screen.keypad(1)
  screen.clear()
  curses.resize_term(46, 150)
  game_win = curses.newwin(40, 135, 3, 7)

  game_win.box()
  game_win.refresh()
  game_win.timeout(1000)
  count = 0
  while count < 5:
    count += 1
    game_win.refresh()
    game_win.addstr(20, 65-count, f'*{"*"*count}>')
    curses.napms(500)


if __name__=='__main__':
  play_snake()