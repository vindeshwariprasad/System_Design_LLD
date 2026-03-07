from abc import ABC, abstractmethod
from Enum import PaymentStatus


class Payment(ABC):
    @abstractmethod
    def process_payment(self, amount):
        pass


class CardPayment(Payment):
    def process_payment(self, amount):
        print(f"Processing card payment of Rs.{amount}")
        return PaymentStatus.PAID


class UPIPayment(Payment):
    def process_payment(self, amount):
        print(f"Processing UPI payment of Rs.{amount}")
        return PaymentStatus.PAID


class CashPayment(Payment):
    def process_payment(self, amount):
        print(f"Processing cash payment of Rs.{amount}")
        return PaymentStatus.PAID
