class User:
    def __init__(self,name,email,calender):
        self.name = name
        self.email = email
        self.calender = calender      ###it is calender of Calender.py
    
    def view_meeting(self):
        return self.calender.show_calender()
    
    def respond_meeting(self,meeting,status):
        meeting.participant[self.email] = status
        
