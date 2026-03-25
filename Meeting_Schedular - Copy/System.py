from Meeting import Meeting

class System:
    _get_instance = None

    def __init__(self,rooms_lest):
        self.room = rooms_lest   ###################list of meetingroom.py
    
    @classmethod
    def get_instance(cls, rooms_lest=None):
        if cls._get_instance is None:
            cls._get_instance = System(rooms_lest)
        return cls._get_instance
        
    def schedule_meeting(self,interval,people,size):
        for i in self.room:
            if i.capacity>=size and i.is_avalable(interval):
                i.book_room(interval)
                meeting = Meeting(id=None, participant_dict=people, interval=interval, room=i, title="Meeting")
                return meeting
        return None

    def cancel_meeting(self, meeting):
        meeting.room.cancel(meeting.interval)
        for email, status in meeting.participant.items():
            meeting.participant[email] = None
