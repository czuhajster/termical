import datetime
import json

import pycal_module


filename = 'pycal_data.json'
with open(filename) as f:
    import_dates = json.load(f)

dates = {}
for date in import_dates:
    dates[datetime.date.fromisoformat(date)] = {}


start_message = "Welcome to PyCal, a Python calendar created by"
start_message += " Arkadiusz Podkowa.\n"
print(start_message)
usage_message = "Get your today's schedule: c\n"
usage_message += "Get events for a specific date: s\n"
usage_message += "Schedule an event: a\n"
usage_message += "Remove an event: r\n"
usage_message += "Reschedule an event: \n"
usage_message += "Change your server's address: \n"
usage_message += "Quit: q"
print(usage_message)

while True:
    action = input('\nWhat do you want to do? ')
    if action == 'c':
        today = pycal_module.get_todays_schedule(dates)
        print(today)
    elif action == 's':
        specific_date = input('Enter specific date (in YYYY MM DD format): ')
        specific_date_schedule = pycal_module.get_specific_date_schedule(dates,
                                                                         specific_date)
        for time, event in specific_date_schedule.items():
            print(f"\t{time}: {event}")
    elif action == 'a':
        specific_date = input('Enter specific date (in YYYY MM DD format): ')
        schedule_event = pycal_module.schedule_event(dates, specific_date)
    elif action == 'r':
        specific_date = input('Enter specific date (in YYYY MM DD format): ')

    elif action == 'q':
        break
