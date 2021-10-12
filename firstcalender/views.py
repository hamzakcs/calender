from django.shortcuts import render
import calendar
from calendar import HTMLCalendar
from datetime import datetime


# Create your views here.
def home(request, year=datetime.now().year, month=datetime.now().strftime("%B")):
    name = "Hamza"

    # capitalize the url input.
    month = month.capitalize()

    # convertin and retrieving the months in number.
    month_number = list(calendar.month_name).index(month)

    # converting to integer.
    month_number = int(month_number)

    # retrieving the actual calender of HTML.
    cal = HTMLCalendar().formatmonth(year, month_number)

    # current year.
    now = datetime.now()
    current_year = now.year

    # Getting time.
    current_time = now.strftime('%I:%M %p %a %d')

    return render(request, 'home.html', {
        'name': name,
        'year': year,
        'month': month,
        'month_number': month_number,
        'cal': cal,
        'current_year': current_year,
        'current_time': current_time,
    })
