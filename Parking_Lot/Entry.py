from Ticket import Ticket


class EntryGate:
    def __init__(self, gate_id, parking_lot):
        self.gate_id = gate_id
        self.parking_lot = parking_lot

    def assign_ticket(self, vehicle):
        spot = self.parking_lot.find_spot(vehicle.vehicle_type)
        spot.add_vehicle(vehicle)
        ticket = Ticket(vehicle, spot, self.gate_id)
        vehicle.ticket = ticket
        print(f"Ticket #{ticket.ticket_id} issued at Gate {self.gate_id} | "
              f"Spot: {spot.spot_type.name}-{spot.spot_id} | "
              f"Vehicle: {vehicle.license_plate}")
        return ticket
