from enum import Enum, auto


class VehicleType(Enum):
    BIKE = auto()
    CAR = auto()
    TRUCK = auto()


class SpotType(Enum):
    SMALL = auto()
    COMPACT = auto()
    LARGE = auto()


class PaymentStatus(Enum):
    PAID = auto()
    FAILED = auto()
    PENDING = auto()


class PaymentMethod(Enum):
    CARD = auto()
    UPI = auto()
    CASH = auto()
