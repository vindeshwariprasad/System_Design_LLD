import time
from Enum import PaymentStatus


class ExitGate:
    def __init__(self, gate_id, fee_calculator):
        self.gate_id = gate_id
        self.fee_calculator = fee_calculator

    def process_exit(self, ticket):
        ticket.exit_time = time.time()
        duration_hours = (ticket.exit_time - ticket.entry_time) / 3600
        ticket.amount = self.fee_calculator.calculate_fee(
            duration_hours, ticket.spot.spot_type
        )
        print(f"Ticket #{ticket.ticket_id} | Duration: {duration_hours:.2f} hrs | "
              f"Amount: Rs.{ticket.amount}")
        return ticket.amount

    def process_payment(self, ticket, payment_method):
        # In real system, integrate with payment gateway
        ticket.payment_status = PaymentStatus.PAID
        ticket.spot.remove_vehicle()
        ticket.vehicle.ticket = None
        print(f"Payment of Rs.{ticket.amount} via {payment_method.name} successful. "
              f"Spot {ticket.spot.spot_id} freed.")
