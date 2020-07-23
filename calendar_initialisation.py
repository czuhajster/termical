import datetime
import calendar
import json

years = [n for n in range(1930, 2101)]
months = [n for n in range(1, 13)]
days = [n for n in range(1, 32)]

dates = {}
thirty_day_months = [4, 6, 9, 11]
thirty_one_day_months = [1, 3, 5, 7, 8, 10, 12]
february = 2
for year in years:
    for month in months:
        if month in thirty_one_day_months:
            for day in days:
                dates[datetime.date(year, month, day)] = {}
        elif month in thirty_day_months:
            for day in days[:30]:
                dates[datetime.date(year, month, day)] = {}
        elif month == february:
            # Chech whether the current year is a leap year.
            leap_year = calendar.isleap(year)
            if leap_year:
                for day in days[:29]:
                    dates[datetime.date(year, month, day)] = {}
            elif leap_year == False:
                for day in days[:28]:
                    dates[datetime.date(year, month, day)] = {}

# Prepare dates to be exported as iso strings.
export_dates = {}
for date in dates:
    export_dates[date.isoformat()] = {}

filename = '/Users/arek/.termical/termical_data.json'
with open(filename, 'w') as f:
    json.dump(export_dates, f, indent=4)
