from input_base import InputBase
from input_base import Keys
from enum import Enum
import os
from time import sleep
from sense_hat import SenseHat


class InputSense(InputBase):
    """
    Input handler for console applications using keyboard input. 
    """
    def __init__(self):
        self._sense = SenseHat()

    def read_key(self) -> Enum:
        """
        Read a key from the console and return its corresponding key code. Method blocks until a key is available.

        Returns:
            Enum: The key code corresponding to the pressed key.
        """
        
        while self._sense.stick.get_events():
            pass
            
        while True:
            for event in self._sense.stick.get_events():
                if event.action == "pressed":
                    if event.direction == "up":
                        return Keys.UP
                    elif event.direction == "down":
                        return Keys.DOWN
                    elif event.direction == "left":
                        return Keys.LEFT
                    elif event.direction == "right":
                        return Keys.RIGHT
                    elif event.direction == "middle":
                        return Keys.ENTER

if __name__ == '__main__':
    print("press any key, ESC to exit")
    c = InputSense()
    while True:
        key = c.read_key()
        print(f"Taste: {key}, Type: {type(key)}")
        if key == Keys.ENTER:
            print("Enter")
        if (key == Keys.ESC):  # Abort with ESC
            break
