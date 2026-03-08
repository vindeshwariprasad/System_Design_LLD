from enum import Enum

class Door(Enum):
    open = 1
    close = 2
    ideal = 3
class Direction(Enum):
    up = 1
    down = 2
    ideal = 3
class CarStatus(Enum):
    up = 1
    down = 2
    maintance = 3
    ideal = 4

