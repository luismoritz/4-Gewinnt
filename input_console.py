from input_base import InputBase
from input_base import Keys
from enum import Enum
import os
from time import sleep

if os.name == 'nt':  # Windows
    import msvcrt
else:  # Posix (Linux, OS X)
    import sys
    import tty
    import termios
    from select import select

class InputConsole(InputBase):
    """
    Input handler for console applications using keyboard input. 
    """

    def read_key(self) -> Enum:
        """
        Read a key from the console and return its corresponding key code. Method blocks until a key is available.

        Returns:
            Enum: The key code corresponding to the pressed key.
        """
        if os.name == 'nt':  # Windows
            key = msvcrt.getch()
            if key in (b'\xe0', b'\x00'):  # Special keys (arrow keys send two bytes)
                key = msvcrt.getch()  # Get the second byte for direction
                if key == b"H":
                    return Keys.UP
                elif key == b"H":
                    return Keys.UP
                elif key == b"P":
                    return Keys.DOWN
                elif key == b"K":
                    return Keys.LEFT
                elif key == b"M":
                    return Keys.RIGHT
                return Keys.UNKNOWN
            elif key == b"\r":
                return Keys.ENTER
            elif key == b"\n":
                return Keys.ENTER
            elif key == b"\x1b":
                return Keys.ESC
            elif key == b"\x03":
                raise KeyboardInterrupt()

        else:
            fd = sys.stdin.fileno()
            old_settings = termios.tcgetattr(fd)
            try:
                tty.setraw(sys.stdin.fileno())
                ch = sys.stdin.read(1)
                if ch == "\x1b":
                    ch = sys.stdin.read(1)
                    if ch == "\x1b":
                        return Keys.ESC
                    ch += sys.stdin.read(1)
                    if ch == "[A":
                        return Keys.UP
                    elif ch == "[B":
                        return Keys.DOWN
                    elif ch == "[C":
                        return Keys.RIGHT
                    elif ch == "[D":
                        return Keys.LEFT
                elif ch == "\r":
                    return Keys.ENTER
                elif ch == "\n":
                    return Keys.ENTER
                elif ch == "\x03":
                    raise KeyboardInterrupt()
                return Keys.UNKNOWN
            finally:
                termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)

if __name__ == '__main__':
    print("press any key, ESC to exit")
    c = InputConsole()
    while True:
        key = c.read_key()
        print(f"Taste: {key}, Type: {type(key)}")
        if key == Keys.ENTER:
            print("Enter")
        if (key == Keys.ESC):  # Abort with ESC
            break
