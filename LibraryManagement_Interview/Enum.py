from enum import Enum, auto


class BookStatus(Enum):
    FREE = auto()
    RESERVED = auto()
    TAKEN = auto()


class AccountStatus(Enum):
    ACTIVE = auto()
    BLOCKED = auto()
