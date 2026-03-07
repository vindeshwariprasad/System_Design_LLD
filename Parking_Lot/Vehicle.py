from abc import ABC
from Enum import VehicleType


class Vehicle(ABC):
    def __init__(self, license_plate, vehicle_type):
        self.license_plate = license_plate
        self.vehicle_type = vehicle_type
        self.ticket = None


class Car(Vehicle):
    def __init__(self, license_plate):
        super().__init__(license_plate, VehicleType.CAR)


class Bike(Vehicle):
    def __init__(self, license_plate):
        super().__init__(license_plate, VehicleType.BIKE)


class Truck(Vehicle):
    def __init__(self, license_plate):
        super().__init__(license_plate, VehicleType.TRUCK)
