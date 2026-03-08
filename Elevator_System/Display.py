from Enum import Direction

class Display:
    def __init__(self):
        self.current_floor = 0
        self.direction = Direction.ideal

    def set_display(self, floor, direction):
        self.current_floor = floor
        self.direction = direction

    def show(self):
        print(f"Floor: {self.current_floor} | Direction: {self.direction.name}")
