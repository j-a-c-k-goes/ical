
# give event a name
# event.name = str(input("enter the name of the event: "))
event.name = "test event"

# event description
event.description = "You have been invited to meet with [name] for [this reason]."

# begin the event
# "year-month-day 00:00:00"
event.begin = datetime.today().strftime("%Y-%m-%d %H:%M:%S")

# end the event (set the duration)
# 1 hour

# location
event.location = "test location"

# add attendees
jack = Attendee("jack@student.gptc.edu", "jack", rsvp=True)
 event.attendees = [jack.email, jack.common_name]

# add url
event.url = "https://www.this.com"

# add a category
event.category = "test category"

# add organizer
event.organizer = "jack@flnpb.com"

# add event to calendar
calendar.events.add(event)

# print the event on the calendar
print(calendar.events)

# output .ics file to folder
with open("../output/invite.ics", "w+") as file:
    print("outputting calendar event")
    file.writelines(calendar.serialize_iter())
