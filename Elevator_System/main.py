

from ElevatorSystem import ElevatorSystem
from Enum import Direction

if __name__ == "__main__":
    system = ElevatorSystem(total_floors=10, num_cars=3)

    # person on floor 3 wants to go up
    print("= Request from Floor 3 (UP) =")
    system.request_elevator(floor_number=3, direction=Direction.up)

    # person inside car 0 presses floor 7
    print("\n= Inside Car 0: Press Floor 7 =")
    system.press_floor_inside_car(car_id=0, floor=7)

    # person on floor 5 wants to go down
    print("\n= Request from Floor 5 (DOWN) =")
    system.request_elevator(floor_number=5, direction=Direction.down)

    # emergency in car 2
    print("\n= Emergency in Car 2 =")
    system.press_emergency(car_id=2)

    # new request should skip car 2 (maintenance)
    print("\n= Request from Floor 1 (UP) - Car 2 skipped =")
    system.request_elevator(floor_number=1, direction=Direction.up)
