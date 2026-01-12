from ansi import Ansi
from game_token import GameToken
from display_base import DisplayBase


class DisplayConsole(DisplayBase):
    def __init__(self):
        Ansi.clear_screen()

    def draw_token(self, x: int, y: int, token: GameToken = GameToken.EMPTY) -> None:
        colors = {'X' : 1, '0' : 3, ' ' : 0}
        if -1 >= y > 6 or 0 >= x > 7:
            return False
        Ansi.gotoXY((x*5)+3+12, ((y+1)*2)+2)
        Ansi.set_foreground(color= colors[token], intensity = False)
        print("██")
        Ansi.reset()

    def draw_grid(self) -> None:
        Ansi.clear_screen()
        Ansi.gotoXY(0,0)
        Ansi.set_foreground(color= 7, intensity = False)
        print("""
              
            ┌────┬────┬────┬────┬────┬────┬────┐
            │    │    │    │    │    │    │    │
            ├────┼────┼────┼────┼────┼────┼────┤
            │    │    │    │    │    │    │    │
            ├────┼────┼────┼────┼────┼────┼────┤
            │    │    │    │    │    │    │    │
            ├────┼────┼────┼────┼────┼────┼────┤
            │    │    │    │    │    │    │    │
            ├────┼────┼────┼────┼────┼────┼────┤
            │    │    │    │    │    │    │    │
            ├────┼────┼────┼────┼────┼────┼────┤
            │    │    │    │    │    │    │    │
            └────┴────┴────┴────┴────┴────┴────┘                         
              """)
        Ansi.reset()

if __name__ == '__main__':
    Ansi.clear_screen()
    Ansi.reset()
    fc = DisplayConsole()
    fc.draw_grid()
    fc.draw_token(0, 0, GameToken.RED)
    fc.draw_token(5, 2, GameToken.YELLOW)
    Ansi.gotoXY(30, 30)
