from LockerStatus import LockerStatus, LockerSize

class Locker:
    def __init__(self,id,size: LockerSize):
        self.id = id
        self.size = size       # LockerSize enum
        self.status = LockerStatus.AVAILABLE
        self.pacakage = None

    def book(self):
        if self.status == LockerStatus.AVAILABLE:
            self.status = LockerStatus.BOOKED
            return True
        return False

    def place_item(self,pacakage):
        if self.status == LockerStatus.BOOKED:
            self.pacakage = pacakage
            self.status = LockerStatus.FILLED
            return True
        return False

    def release(self):
        if self.status == LockerStatus.FILLED:
            item = self.pacakage
            self.pacakage = None
            self.status = LockerStatus.AVAILABLE
            return item
        return None

    def is_available(self):
        return self.status == LockerStatus.AVAILABLE
