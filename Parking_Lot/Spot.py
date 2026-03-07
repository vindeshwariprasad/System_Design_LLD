from abc import ABC
from Enum import SpotType


class ParkingSpot(ABC):
    def __init__(self, spot_id, spot_type):
        self.spot_id = spot_id
        self.spot_type = spot_type
        self.is_free = True
        self.vehicle = None

    def add_vehicle(self, vehicle):
        if not self.is_free:
            raise Exception(f"Spot {self.spot_id} is already occupied")
        self.vehicle = vehicle
        self.is_free = False

    def remove_vehicle(self):
        self.vehicle = None
        self.is_free = True


class SmallSpot(ParkingSpot):
    def __init__(self, spot_id):
        super().__init__(spot_id, SpotType.SMALL)


class CompactSpot(ParkingSpot):
    def __init__(self, spot_id):
        super().__init__(spot_id, SpotType.COMPACT)


class LargeSpot(ParkingSpot):
    def __init__(self, spot_id):
        super().__init__(spot_id, SpotType.LARGE)
