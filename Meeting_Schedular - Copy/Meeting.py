from Status import Status
class Meeting:
    def __init__(self,id,participant_dict, interval, room, title):
        self.id = id
        self.participant = participant_dict    ##### {user.email:Status}
        self.interval = interval
        self.room = room       #########meeting.py
        self.title = title
    
    def add_participant(self,user):
        if user not in self.participant:
            self.participant[user] = Status.Pending
            print("send")
        else:
            print("user already present") 
        
    def remove_participant(self,user):
        user.calender.remove_interval(self.interval)
        del self.participant[user.email]
        print("participant removed")
    
    def see_status(self):
        return self.participant


        