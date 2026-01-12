from player_console import PlayerConsole
from game_token import GameToken
from game_logic import GameLogicLocal
from game_state import GameState
from game_logic_client import GameLogicClient
import time

class Coordinator:
    def __init__(self, game=None, player_RED=None, player_YELLOW=None):
        self._game = game
        self._player_RED = player_RED
        self._player_YELLOW = player_YELLOW      

    def run(self):
        while True:
            state = self._game.get_state()
            board = self._game.get_board()
            if state != GameState.TURN_RED and state != GameState.TURN_YELLOW:
                if self._player_RED is not None:
                    self._player_RED.draw_board(board, state)
                if self._player_YELLOW is not None:
                    self._player_YELLOW.draw_board(board, state)
                break
            if state == GameState.TURN_RED:
                if self._player_RED is None:
                    self._player_YELLOW.draw_board(board, state)
                    while True:
                        if self._game.get_state() != GameState.TURN_RED:
                            break
                else:  
                    self._player_RED.draw_board(board, state)
                    column = self._player_RED.play_turn()  
                    self._game.drop_token(GameToken.RED, column)
            if state == GameState.TURN_YELLOW:
                if self._player_YELLOW is None:
                    self._player_RED.draw_board(board, state)
                    while True:
                        if self._game.get_state() != GameState.TURN_YELLOW:
                            break
                else:
                    self._player_YELLOW.draw_board(board, state)
                    column = self._player_YELLOW.play_turn()
                    self._game.drop_token(GameToken.YELLOW, column)
            time.sleep(0.5)

if __name__ == '__main__':
    url = ""
    player = True
    local_input = input("Local (L) or Remote (R)? ").strip().upper()
    if local_input == "L":
        game = GameLogicLocal()
        player_RED = PlayerConsole(GameToken.RED)
        player_YELLOW = PlayerConsole(GameToken.YELLOW)
    else:
        url = input("Enter URL: ")
        game = GameLogicClient(host=url)
        player_input = input("Play as Red (R) or Yellow (Y)? ").strip().upper()
        if player_input == "R":
            player_RED = PlayerConsole(GameToken.RED)
            player_YELLOW = None
        else:
            player_RED = None
            player_YELLOW = PlayerConsole(GameToken.YELLOW)
    print("Welcome to Connect 4, starting game...")
    coordinator = Coordinator(game, player_RED, player_YELLOW)
    coordinator.run()
