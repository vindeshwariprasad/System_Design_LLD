from User import User

class Organizer(User):
    def __init__(self, name, email, calender, system):
        super().__init__(name, email, calender)
        self.system = system

    def schedule_meeting(self,interval,people,size):
        return self.system.schedule_meeting(interval, people, size)

    def cancel_meeting(self,meeting):
        self.system.cancel_meeting(meeting)

    def add_people(self,meeting,user):
        meeting.add_participant(user)

    def remove_people(self,meeting,user):
        meeting.remove_participant(user)
    

