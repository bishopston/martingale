import calendar
from datetime import datetime

def front_month_calc(date_str):
    c = calendar.Calendar(firstweekday=calendar.SUNDAY)

    year = date_str.year
    next_year = 0

    month = date_str.month
    next_month = 0

    if month == 12:
        next_month = 1
        next_year = year + 1
    else:
        next_month = month + 1
        next_year = year

    monthcal = c.monthdatescalendar(year,month)
    next_monthcal = c.monthdatescalendar(next_year,next_month)

    third_friday_same_month = [day for week in monthcal for day in week if
                day.weekday() == calendar.FRIDAY and
                day.month == month][2]


    third_friday_next_month = [day for week in next_monthcal for day in week if
                day.weekday() == calendar.FRIDAY and
                day.month == next_month][2]


    if date_str <= third_friday_same_month:
        return third_friday_same_month
    else:
        return third_friday_next_month
