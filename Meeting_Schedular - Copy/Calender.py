class Calender:
    def __init__(self,id,intervals):
        self.id = id
        self.__intervals = intervals ###list of interval

    
    def show_calender(self):
        return self.__intervals
    
    def allow(self,interval):     ####checking for user to allow meeting
        for existing in self.__intervals:
            if interval.start < existing.end and interval.end > existing.start:
                return False
        return True
    
    def add_interval(self,interval):
        if self.allow(interval):
            self.__intervals.append(interval)
            print("Interval added")
        else:
            print("there is over lap")
    def remove_interval(self,interval):
        self.__intervals.remove(interval)
    
    
        