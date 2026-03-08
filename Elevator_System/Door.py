from Enum import Door as DoorState

class Door:
    def __init__(self):
        self.state = DoorState.close

    def open_door(self):
        if self.state != DoorState.open:
            self.state = DoorState.open
            print("Door opened")

    def close_door(self):
        if self.state != DoorState.close:
            self.state = DoorState.close
            print("Door closed")

    def get_state(self):
        return self.state
