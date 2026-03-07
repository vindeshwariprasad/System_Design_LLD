class ParkingLot:
    _instance = None

    def __init__(self):
        self.floors = []
        self.entry_gates = []
        self.exit_gates = []

    @classmethod
    def get_instance(cls):
        if cls._instance is None:
            cls._instance = ParkingLot()
        return cls._instance

    def add_floor(self, floor):
        self.floors.append(floor)

    def add_entry_gate(self, gate):
        self.entry_gates.append(gate)

    def add_exit_gate(self, gate):
        self.exit_gates.append(gate)

    def find_spot(self, vehicle_type):
        """Search all floors for an available spot."""
        for floor in self.floors:
            spot = floor.find_available_spot(vehicle_type)
            if spot:
                return spot
        raise Exception("No available spot for this vehicle type")
