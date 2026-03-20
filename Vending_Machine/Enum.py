from enum import Enum

class ProductType(Enum):
    Sweet = 1
    Salty = 2
    Cream = 3

class VendingState(Enum):
    Idle = 1
    MoneyInserted = 2
    ProductSelected = 3
    Dispensing = 4
