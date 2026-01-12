from display_sense import DisplaySense
from input_sense import InputSense
from player_base import PlayerBase
from game_state import GameState
from game_token import GameToken
from ansi import Ansi
from input_base import Keys

class PlayerSense(PlayerBase):
    def __init__(self, player: GameToken):  # Red or Yellow player
        super().__init__(player)
        self._display = DisplaySense() # use this class for console output
        self._input = InputSense() # use this class for console inputq

    def play_turn(self) -> int:
        column = 3
        self._display.draw_token(column, -1, self._player)
        while True:
            key = self._input.read_key()
            if key == Keys.LEFT and column > 0:
                self._display.draw_token(column, -1, GameToken.EMPTY)
                column -= 1
            if key == Keys.RIGHT and column < 6:
                self._display.draw_token(column, -1, GameToken.EMPTY)
                column += 1
            if key == Keys.ENTER:
                self._display.draw_token(column, -1, GameToken.EMPTY)
                return column
            self._display.draw_token(column, -1, self._player)
        
    def draw_board(self, board: list, state: GameState):
        self._display.draw_grid(6, 7)
        if (state == GameState.TURN_RED and self.player == GameToken.RED) or (state == GameState.TURN_YELLOW and self.player == GameToken.YELLOW):
            self._display.draw_token(self.current_column, -1, self.player)
        for row in range(6):
            for column in range(7):
                self._display.draw_token(column, row, board[row][column])

if __name__ == '__main__':
    board = [[' ' for _ in range(7)] for _ in range(6)]
    board[5][6] = GameToken.RED  # [Y][X]
    p = PlayerSense(GameToken.YELLOW)
    Ansi.clear_screen()
    Ansi.reset()
    p.draw_board(board, GameState.TURN_YELLOW)
    pos = p.play_turn()
    Ansi.reset()
    Ansi.gotoXY(1, 30)
    print(f"Position: {pos}")
