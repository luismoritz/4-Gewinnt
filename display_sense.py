from ansi import Ansi
from game_token import GameToken
from display_base import DisplayBase
from sense_hat import SenseHat

class DisplaySense(DisplayBase): 
    def __init__(self):
        Ansi.clear_screen()
        self._sense = SenseHat()

    def draw_token(self, column: int, row: int, token: GameToken = GameToken.EMPTY) -> None:
        if(token == GameToken.RED):
            color = (255, 0, 0)
        elif(token == GameToken.YELLOW):
            color = (255, 255, 0)
        elif(token == GameToken.EMPTY):
            color = (0, 0, 0)
        self._sense.set_pixel(column, row+1, color)
        

    def draw_grid(self, rows, columns) -> None:
        for i in range(7):
            for j in range(7):
                self._sense.set_pixel(i, j, (0, 0, 0))
        for i in range(8):
            self._sense.set_pixel(7, i, (100, 100, 100))
            self._sense.set_pixel(i, 7, (100, 100, 100))                      

if __name__ == '__main__':
    Ansi.clear_screen()
    Ansi.reset()
    fc = DisplaySense()
    fc.draw_grid(6,7)
    fc.draw_token(0, 0, GameToken.RED)
    fc.draw_token(5, 2, GameToken.YELLOW)
    print(type(GameToken.RED))
    print(GameToken.RED)
