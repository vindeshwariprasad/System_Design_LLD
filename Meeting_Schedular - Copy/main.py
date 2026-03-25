from Interval import Interval
from Calender import Calender
from User import User
from Organizer import Organizer
from Meetingroom import Meetingroom
from System import System
from Status import Status

# Create intervals and calendars
cal1 = Calender(id=1, intervals=[])
cal2 = Calender(id=2, intervals=[])
cal3 = Calender(id=3, intervals=[])

# Create users
user1 = User(name="Alice", email="alice@mail.com", calender=cal1)
user2 = User(name="Bob", email="bob@mail.com", calender=cal2)

# Create meeting rooms
room1 = Meetingroom(id=1, capacity=5, is_available=True, intervals=[], meeting=None)
room2 = Meetingroom(id=2, capacity=10, is_available=True, intervals=[], meeting=None)

# Create system with rooms
system = System(rooms_lest=[room1, room2])

organizer = Organizer(name="Charlie", email="charlie@mail.com", calender=cal3, system=system)

# Create an interval for the meeting
meeting_interval = Interval(id=1, start="10:00", end="11:00")

# Participants dict {email: Status}
people = {
    user1.email: Status.Pending,
    user2.email: Status.Pending
}

# Try scheduling via system (Note: allow() is not implemented so is_avalable returns False)
meeting = system.schedule_meeting(interval=meeting_interval, people=people, size=3)
if meeting:
    print(f"Meeting scheduled in room {meeting.room.id}")
else:
    print("No room available via system (allow() not implemented yet)")

# Direct booking to demo the flow
print("\n--- Direct booking demo ---")
booked = room1.book_room(meeting_interval)
print(f"Room 1 booked: {booked}")

from Meeting import Meeting
meeting = Meeting(id=1, participant_dict=people, interval=meeting_interval, room=room1, title="Team Sync")
print(f"Meeting created: {meeting.title}")

# Organizer adds a participant
organizer.add_people(meeting, "dave@mail.com")

# Check participant status
print(f"Participants: {meeting.see_status()}")

# User responds to meeting
user1.respond_meeting(meeting, Status.Accept)
print(f"After Alice accepts: {meeting.see_status()}")

# Cancel meeting
system.cancel_meeting(meeting)
print(f"Meeting cancelled, room1 intervals: {room1.intervals}")
