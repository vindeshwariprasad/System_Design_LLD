from Floor import Floor

class Building:
    def __init__(self, total_floors=15):
        self.total_floors = total_floors
        self.floors = [Floor(i) for i in range(total_floors)]

    def get_floor(self, floor_number):
        if 0 <= floor_number < self.total_floors:
            return self.floors[floor_number]
        return None
