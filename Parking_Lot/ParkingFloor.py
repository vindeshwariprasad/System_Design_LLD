from Enum import SpotType, VehicleType


# Maps each vehicle type to compatible spot type
VEHICLE_TO_SPOT = {
    VehicleType.BIKE: SpotType.SMALL,
    VehicleType.CAR: SpotType.COMPACT,
    VehicleType.TRUCK: SpotType.LARGE,
}


class ParkingFloor:
    def __init__(self, floor_id):
        self.floor_id = floor_id
        # dict of SpotType -> list of ParkingSpot
        self.spots = {spot_type: [] for spot_type in SpotType}

    def add_spot(self, spot):
        self.spots[spot.spot_type].append(spot)

    def find_available_spot(self, vehicle_type):
        """Find first free spot matching the vehicle type."""
        spot_type = VEHICLE_TO_SPOT.get(vehicle_type)
        if spot_type is None:
            return None
        for spot in self.spots[spot_type]:
            if spot.is_free:
                return spot
        return None
