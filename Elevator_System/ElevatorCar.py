from Enum import CarStatus, Direction, Door as DoorState
from Button import Floor_Button, Door_Button, Emergency_Button
from Door import Door
from Display import Display

class ElevatorCar:
    def __init__(self, car_id, total_floors=15):
        self.car_id = car_id
        self.current_floor = 0
        self.status = CarStatus.ideal
        self.direction = Direction.ideal
        self.total_floors = total_floors

        self.door = Door()
        self.display = Display()
        self.floor_button = Floor_Button(floor=total_floors)
        self.open_button = Door_Button(button_type="open")
        self.close_button = Door_Button(button_type="close")
        self.emergency_button = Emergency_Button()

    def press_floor(self, floor):
        if 0 <= floor < self.total_floors:
            self.floor_button.press_floor_button(floor)
            print(f"Car {self.car_id}: Floor {floor} requested")

    def press_open(self):
        self.open_button.press()
        self.door.open_door()

    def press_close(self):
        self.close_button.press()
        self.door.close_door()

    def press_emergency(self):
        self.emergency_button.press()
        self.status = CarStatus.maintance

    def move_to_floor(self, target_floor):
        if target_floor > self.current_floor:
            self.direction = Direction.up
            self.status = CarStatus.up
        elif target_floor < self.current_floor:
            self.direction = Direction.down
            self.status = CarStatus.down
        else:
            return

        print(f"Car {self.car_id}: Moving from floor {self.current_floor} to {target_floor}")
        self.current_floor = target_floor
        self.display.set_display(self.current_floor, self.direction)
        self.display.show()

        self.floor_button.reset_floor_button(target_floor)
        self.door.open_door()

    def process_requests(self):
        pressed = self.floor_button.get_pressed_floors()
        if not pressed:
            self.status = CarStatus.ideal
            self.direction = Direction.ideal
            self.display.set_display(self.current_floor, self.direction)
            return

        if self.direction == Direction.up or self.direction == Direction.ideal:
            above = [f for f in pressed if f > self.current_floor]
            below = [f for f in pressed if f < self.current_floor]
            if above:
                self.move_to_floor(min(above))
            elif below:
                self.move_to_floor(max(below))
        else:
            below = [f for f in pressed if f < self.current_floor]
            above = [f for f in pressed if f > self.current_floor]
            if below:
                self.move_to_floor(max(below))
            elif above:
                self.move_to_floor(min(above))

    def is_idle(self):
        return self.status == CarStatus.ideal
