""" 
    program name: python script to make ical events (early-build)

    date modified: 07 september 2022

    have not figured out yet: timezone change to local

    links used: https://www.programiz.com/python-programming/datetime
                https://www.geeksforgeeks.org/python-datetime-module/
                https://www.guru99.com/date-time-and-datetime-classes-in-python.html
                https://icspy.readthedocs.io/en/stable/                
"""

# import modules
from ics import Calendar, Event, Attendee
from datetime import datetime, timedelta
from icalendar import LocalTimezone

# create instances of calendar and event, local timezone
calendar = Calendar()
event = Event()
lt = LocalTimezone()

# invite class 
class Invite(calendar, event):
    
    def __init__(self, calendar, event):
        self.calendar = calendar
        self.event = event
    
    def name(self):
        print("EVENT NAME:")
        event.name = str(input("name of calendar event: "))
        return event.name
        
    def desc(self):
        print("EVENT DESCRIPTION:")
        event.description = str(input("calendar event's description: "))
        return event.description
    
    def begin(self):
        print("EVENT TIME:")
        year = 2022
        month = int(input("month (1-12): "))
        day = int(input("day: (1-31): "))
        hour = int(input("hour (1-24): "))
        minute = int(input("minute (1-59): "))
        second = 0
        event.begin = datetime(year, month, day, hour, minute, second).strftime("%Y-%m-%d %H:%M:%S")
        # event.begin = datetime.today().strftime("%Y-%m-%d %H:%M:%S")
        return event.begin
    
    def duration(self, n:int=1):
        print("EVENT DURATIONS:")
        underAnHour = bool
        timeLimit = str(input("is this event under an hour (y/n): "))
        if timeLimit.lower() == "y":
            underAnHour = True
        if underAnHour is True:
            n = int(input("length of event (in minutes): "))
            event.duration = timedelta(minutes=n)
            return event.duration 
        else:
            print("setting event for at least one hour")
            n = int(input("length of event (in minutes): "))
            event.duration = timedelta(hours=n)
            return event.duration
    
    def location(self):
        event.location = str(input("location of the event: "))
        return event.location
    
    def url(self):
        event.url = str(input("url for event: "))
        # checkhttp(event.url)
        return event.url
    
    def attending(self):
        adding = true
        added = []
        while adding:
            print("NEW ATTENDEE:")
            email = str(input("email address: "))
            name = str(input("name: "))
            newattendee = Attendee(email,name, rsvp=True)
            attendee = { newattendee }
            added.append(attendee)
            print("attendee added.")
            confirm = str(input("still adding attendees (y/n)? "))
            if confirm.lower() == "n":
                adding = False
                break
            elif confirm.lower() == "y":
                print("adding more attendees")
            else:
                raise ValueError("confirmation input incorrect. please use 'y' or 'n' ")
                continue
        return added

    def category(self):
        event.category = str(input("category: "))
        return event.catergory
        
    def organizer(self):
        # organizer should ultimately be self, attendee[0]
        event.organizer = str(input("organizer(email): "))
        return event.organizer
    
    def prep_event(self, calandar, event):
        prep = calendar.events.add(event)
        return prep
    
    def to_ical(self, calendar):
        filename = str(input("name for file (example: big ass bday party): "))
        filename = filename.replace(" ", -) # replace spaces with hypens for file name sanitization
        with open(f"..output/{filename}.ics", "w+") as file:
            file.writelines(calendar.serialize_iter())
            print(filename, "written to output folder")