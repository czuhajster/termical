import datetime

def get_todays_schedule(dates):
    """Retrieve the shedule for today from `dates` object."""
    today = datetime.date.today()
    todays_schedule = dates[today]
    return todays_schedule

def get_specific_date_schedule(dates, specific_date):
    """Retrieve the shedule for the specific date from `dates` object."""
    year = int(specific_date[:4])
    month = int(specific_date[5:7])
    day = int(specific_date[8:])
    specific_date = datetime.date(year, month, day)
    specific_date_schedule = dates[specific_date]
    return specific_date_schedule

def schedule_event(dates, schedule_date):
    """Schedule an event for the specific date."""
    year = int(schedule_date[:4])
    month = int(schedule_date[5:7])
    day = int(schedule_date[8:])
    event = input('Enter an event: ')
    time = input('Enter the time of the event (in HH MM format): ')
    hour = int(time[:2])
    minute = int(time[3:])
    event_time = datetime.time(hour, minute)
    dates[datetime.date(year, month, day)][event_time] = event

def remove_event(dates, remove_event_date):
    """Remove an event taking place on specific date."""
    year = int(schedule_date[:4])
    month = int(schedule_date[5:7])
    day = int(schedule_date[8:])




