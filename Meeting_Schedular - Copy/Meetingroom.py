class Meetingroom:
    def __init__(self,id,capacity,is_available,intervals,meeting):
        self.id = id
        self.capacity = capacity
        self.is_available = is_available
        self.intervals = intervals

    def allow(self,interval):
        for existing in self.intervals:
            if interval.start < existing.end and interval.end > existing.start:
                return False
        return True
    def book_room(self,interval):
        if self.is_available and self.allow(interval):
            self.intervals.append(interval)
            return True
        else:
            return False
    def is_avalable(self,interval):
        if self.allow(interval):
            return True
        else:
            return False
    
    def cancel(self, interval):
        self.intervals.remove(interval)

        
    