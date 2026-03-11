from enum import Enum

class LockerStatus(Enum):
    AVAILABLE = "available"
    BOOKED = "booked"
    FILLED = "filled"

class LockerSize(Enum):
    SMALL = 1
    MEDIUM = 2
    LARGE = 3
    XLARGE = 4
