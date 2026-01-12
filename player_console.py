from display_base import DisplayBase  # base class for output methods
from input_console import InputConsole
from display_console import DisplayConsole
from player_base import PlayerBase
from game_state import GameState
from game_token import GameToken
from ansi import Ansi
#Self imported
from input_base import Keys
import time

class PlayerConsole(PlayerBase):
    def __init__(self, player: GameToken):  # Red or Yellow player
        super().__init__(player)
        self._input = InputConsole() # use this class for console input
        self._current_column = 0
        self._display = DisplayConsole() # use this class for console output

    def play_turn(self) -> int:
        while True:
            movements = {Keys.LEFT : -1, Keys.RIGHT : 1}
            key = self._input.read_key()
            if not key:
                time.sleep(0.01)
                continue
            if key == Keys.ENTER or key == Keys.DOWN:
                return self._current_column
            if key in movements:
                if 0 <= (self._current_column + movements[key]) <= 6:
                    self._display.draw_token(self._current_column, -1, GameToken.EMPTY)
                    self._current_column += movements[key]
                    self._display.draw_token(self._current_column, -1, self._player)

    def draw_board(self, board: list, state: GameState):
        self._display.draw_grid()
        if (state == GameState.TURN_RED and self._player == GameToken.RED) or (state == GameState.TURN_YELLOW and self._player == GameToken.YELLOW):
            self._display.draw_token(self._current_column, -1, self._player)
        elif state == GameState.TURN_RED or state == GameState.TURN_YELLOW:
            print("\nWaiting for other player...\n")
        converter = {"X": GameToken.RED, "0": GameToken.YELLOW}        
        for row, arr_row in enumerate(board):
            for column, val_column in enumerate(arr_row):
                if val_column != " ":
                    self._display.draw_token(column, row, converter[val_column])
        if state == GameState.WON_RED:
            print("\nRed player won!\n")
        if state == GameState.WON_YELLOW:
            print("\nYellow player won!\n")
        if state == GameState.DRAW:
            print("\nIt's a draw!\n")
        return
    

if __name__ == '__main__':
    board = [[' ' for _ in range(7)] for _ in range(6)]
    board[5][0] = GameToken.RED  # [Y][X]
    p = PlayerConsole(GameToken.YELLOW)
    Ansi.clear_screen()
    Ansi.reset()
    p.draw_board(board, GameState.TURN_YELLOW)
    pos = p.play_turn()
    Ansi.reset()
    Ansi.gotoXY(1, 20)
    print(f"Position: {pos}")
