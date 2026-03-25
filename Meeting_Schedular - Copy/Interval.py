class Interval:
    def __init__(self,id,start,end):
        self.start = start
        self.end = end
        self.id = id

    def get_interval(self):
        return [self.start,self.end]
    
        