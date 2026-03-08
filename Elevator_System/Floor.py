from Button import Hall_Button
from Display import Display
from Enum import Direction

class Floor:
    def __init__(self, floor_number):
        self.floor_number = floor_number
        self.display = Display()
        self.up_button = Hall_Button(direction=Direction.up)
        self.down_button = Hall_Button(direction=Direction.down)

    def press_up(self):
        self.up_button.press()
        print(f"Floor {self.floor_number}: UP button pressed")
        return self.floor_number, Direction.up

    def press_down(self):
        self.down_button.press()
        print(f"Floor {self.floor_number}: DOWN button pressed")
        return self.floor_number, Direction.down

    def update_display(self, floor, direction):
        self.display.set_display(floor, direction)

    def reset_buttons(self, direction):
        if direction == Direction.up:
            self.up_button.reset()
        else:
            self.down_button.reset()
