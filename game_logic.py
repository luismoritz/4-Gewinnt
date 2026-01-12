from game_state import GameState
from game_token import GameToken
from drop_state import DropState
from game_logic_base import GameLogicBase
import time

class GameLogicLocal(GameLogicBase):
    ROWS = 6
    COLS = 7

    def __init__(self):
        self._board = [[" "," "," "," "," "," "," "],
                      [" "," "," "," "," "," "," "],
                      [" "," "," "," "," "," "," "],
                      [" "," "," "," "," "," "," "],
                      [" "," "," "," "," "," "," "],
                      [" "," "," "," "," "," "," "]]
        self._state = GameState.TURN_RED # current game state
        
    def get_board(self) -> list:
        return self._board

    def get_state(self) -> GameState:
        return self._state
    
    def check4(self, x, y, player):
        directions = [(1, 0), (0, 1), (1, 1), (1, -1)]  # vertical, horizontal, diagonals

        def count(dx, dy):
            cnt = 0
            for step in range(1, 4):
                nx, ny = x + dx * step, y + dy * step
                if 0 <= nx < 6 and 0 <= ny < 7 and self._board[nx][ny] == player:
                    cnt += 1
                else:
                    break
            return cnt

        for dx, dy in directions:
            forward = count(dx, dy)
            backward = count(-dx, -dy)
            total = forward + backward + 1  # +1 for the current piece
            if total >= 4:
                return True
        return False 
    
    def drop_token(self, player: GameToken, column: int) -> DropState:
        if self._state == GameState.TURN_RED and player != GameToken.RED:
            return DropState.WRONG_PLAYER
        elif self._state == GameState.TURN_YELLOW and player != GameToken.YELLOW:
            return DropState.WRONG_PLAYER
        if 0 > column > 6:
            return DropState.COLUMN_INVALID
        if self._board[0][column] != " ":
            return DropState.COLUMN_FULL
        for row in range(5,-1,-1):
            if self._board[row][column] == " ":
                self._board[row][column] = player.value
                if self.check4(row, column, player):
                    converter = {GameToken.RED: GameState.WON_RED, GameToken.YELLOW: GameState.WON_YELLOW}
                    self._state = converter[player]
                elif all(self._board[0][col] != " " for col in range(7)):
                    self._state = GameState.DRAW
                else:
                    if player == GameToken.RED:
                        self._state = GameState.TURN_YELLOW
                    else:
                        self._state = GameState.TURN_RED
                break
        return DropState.DROP_OK

if __name__ == '__main__':
    l = GameLogicLocal()
    #print(l.get_board())
    l.drop_token(GameToken.RED, 1)
    print(l.get_board())
    