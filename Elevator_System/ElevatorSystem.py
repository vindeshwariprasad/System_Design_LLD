from Building import Building
from ElevatorCar import ElevatorCar
from Enum import Direction

class ElevatorSystem:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self, total_floors=15, num_cars=3):
        if hasattr(self, '_initialized'):
            return
        self._initialized = True
        self.building = Building(total_floors)
        self.cars = [ElevatorCar(car_id=i, total_floors=total_floors) for i in range(num_cars)]

    def request_elevator(self, floor_number, direction):
        floor = self.building.get_floor(floor_number)
        if not floor:
            print(f"Invalid floor: {floor_number}")
            return

        if direction == Direction.up:
            floor.press_up()
        else:
            floor.press_down()

        best_car = self._dispatch(floor_number, direction)
        if best_car:
            print(f"Dispatching Car {best_car.car_id} to floor {floor_number}")
            best_car.move_to_floor(floor_number)
            floor.reset_buttons(direction)

    def _dispatch(self, floor_number, direction):
        best_car = None
        min_distance = float('inf')

        for car in self.cars:
            if car.status.name == "maintance":
                continue

            distance = abs(car.current_floor - floor_number)

            # prefer idle cars
            if car.is_idle():
                if distance < min_distance:
                    min_distance = distance
                    best_car = car
            # prefer cars moving towards the requested floor
            elif car.direction == Direction.up and direction == Direction.up and car.current_floor <= floor_number:
                if distance < min_distance:
                    min_distance = distance
                    best_car = car
            elif car.direction == Direction.down and direction == Direction.down and car.current_floor >= floor_number:
                if distance < min_distance:
                    min_distance = distance
                    best_car = car

        # fallback: pick closest car that's not in maintenance
        if not best_car:
            for car in self.cars:
                if car.status.name != "maintance":
                    distance = abs(car.current_floor - floor_number)
                    if distance < min_distance:
                        min_distance = distance
                        best_car = car

        return best_car

    def press_floor_inside_car(self, car_id, floor):
        if 0 <= car_id < len(self.cars):
            self.cars[car_id].press_floor(floor)
            self.cars[car_id].process_requests()

    def press_emergency(self, car_id):
        if 0 <= car_id < len(self.cars):
            self.cars[car_id].press_emergency()
            print(f"Car {car_id} is now in maintenance mode")
