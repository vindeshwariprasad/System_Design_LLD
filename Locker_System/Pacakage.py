from LockerStatus import LockerSize

class Pacakage:
    def __init__(self,id,size: LockerSize,arrival_date):
        self.id = id
        self.size = size       # LockerSize enum
        self.date = arrival_date
