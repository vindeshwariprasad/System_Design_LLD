class Lockerrrom:
    def __init__(self,id,lockers):
        self.id = id
        self.lockers = lockers #list of locker

    def find_available_locker(self,size):
        # find smallest available locker that fits the package
        best = None
        for locker in self.lockers:
            if locker.is_available() and locker.size.value >= size.value:
                if best is None or locker.size.value < best.size.value:
                    best = locker
        return best

    def get_all_available(self):
        return [l for l in self.lockers if l.is_available()]
