import time
from Enum import PaymentStatus


class Ticket:
    counter = 0

    def __init__(self, vehicle, spot, entry_gate_id):
        Ticket.counter += 1
        self.ticket_id = Ticket.counter
        self.vehicle = vehicle
        self.spot = spot
        self.entry_time = time.time()
        self.exit_time = None
        self.entry_gate_id = entry_gate_id
        self.payment_status = PaymentStatus.PENDING
        self.amount = 0
