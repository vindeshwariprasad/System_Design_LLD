import time
from ParkingLot import ParkingLot
from ParkingFloor import ParkingFloor
from Spot import SmallSpot, CompactSpot, LargeSpot
from Vehicle import Car, Bike, Truck
from Entry import EntryGate
from Exit import ExitGate
from FeeCalculator import HourlyFeeCalculator
from Enum import PaymentMethod


def main():
    # 1. Setup: Create parking lot (Singleton)
    parking_lot = ParkingLot.get_instance()

    # 2. Create a floor and add spots
    floor1 = ParkingFloor(floor_id=1)
    floor1.add_spot(SmallSpot(spot_id=1))
    floor1.add_spot(SmallSpot(spot_id=2))
    floor1.add_spot(CompactSpot(spot_id=3))
    floor1.add_spot(CompactSpot(spot_id=4))
    floor1.add_spot(LargeSpot(spot_id=5))
    parking_lot.add_floor(floor1)

    # 3. Create gates
    fee_calculator = HourlyFeeCalculator()
    entry_gate = EntryGate(gate_id=1, parking_lot=parking_lot)
    exit_gate = ExitGate(gate_id=1, fee_calculator=fee_calculator)
    parking_lot.add_entry_gate(entry_gate)
    parking_lot.add_exit_gate(exit_gate)

    # 4. Vehicles enter
    print("=== VEHICLES ENTERING ===")
    car1 = Car("KA-01-1234")
    ticket1 = entry_gate.assign_ticket(car1)

    bike1 = Bike("KA-02-5678")
    ticket2 = entry_gate.assign_ticket(bike1)

    truck1 = Truck("KA-03-9999")
    ticket3 = entry_gate.assign_ticket(truck1)

    # 5. Simulate time passing
    print("\n... time passes ...\n")
    time.sleep(2)

    # 6. Vehicles exit
    print("=== VEHICLES EXITING ===")
    exit_gate.process_exit(ticket1)
    exit_gate.process_payment(ticket1, PaymentMethod.CARD)

    print()
    exit_gate.process_exit(ticket2)
    exit_gate.process_payment(ticket2, PaymentMethod.UPI)

    print()
    exit_gate.process_exit(ticket3)
    exit_gate.process_payment(ticket3, PaymentMethod.CASH)

    # 7. Spot status after exit
    print(f"\n=== SPOT STATUS ===")
    for spot_type, spots in floor1.spots.items():
        for spot in spots:
            status = "FREE" if spot.is_free else "OCCUPIED"
            print(f"Spot {spot.spot_id} ({spot_type.name}): {status}")

    # 8. Parking full scenario
    print("\n=== PARKING FULL TEST ===")
    car2 = Car("KA-04-1111")
    car3 = Car("KA-05-2222")
    entry_gate.assign_ticket(car2)
    entry_gate.assign_ticket(car3)
    try:
        car4 = Car("KA-06-3333")
        entry_gate.assign_ticket(car4)  
    except Exception as e:
        print(f"Expected error: {e}")


if __name__ == "__main__":
    main()
