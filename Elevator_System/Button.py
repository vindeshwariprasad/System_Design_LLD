from abc import abstractmethod, ABC

class Button(ABC):
    def __init__(self, pressed=False):
        self.pressed = pressed

    def get_button_status(self):
        return self.pressed

    def press(self):
        self.pressed = True

    def reset(self):
        self.pressed = False

class Floor_Button(Button):
    def __init__(self, pressed=False, floor=15):
        super().__init__(pressed)
        self.floor = [False for x in range(floor)]

    def press_floor_button(self, floors):
        if self.floor[floors] == False:
            self.floor[floors] = True

    def reset_floor_button(self, floors):
        self.floor[floors] = False

    def get_pressed_floors(self):
        return [i for i, pressed in enumerate(self.floor) if pressed]

class Hall_Button(Button):
    def __init__(self, direction, pressed=False):
        super().__init__(pressed)
        self.direction = direction  # Direction.up or Direction.down

class Door_Button(Button):
    def __init__(self, button_type, pressed=False):
        super().__init__(pressed)
        self.button_type = button_type  # "open" or "close"

class Emergency_Button(Button):
    def __init__(self, pressed=False):
        super().__init__(pressed)

    def press(self):
        self.pressed = True
        print("EMERGENCY: Operator has been notified!")
