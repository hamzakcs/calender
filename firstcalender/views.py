import calendar
from calendar import HTMLCalendar
from datetime import datetime

from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, HttpResponse

from .models import Event, venue
from .forms import venue_form, event_form

import csv

from django.http import FileResponse
import io
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
from reportlab.lib.pagesizes import letter


# Create your views here.
def venue_file_pdf(request):
    Venue = venue.objects.all()
    # Create Byte stream Buffer
    buf = io.BytesIO()
    # Create a canvas
    c = canvas.Canvas(buf, pagesize=letter, bottomup=0)
    # Create Text Object
    textob = c.beginText()
    textob.setTextOrigin(inch, inch)
    textob.setFont('Helvetica', 14)

    lines = []
    for venues in Venue:
        lines.append(venues.name)
        lines.append(venues.address)
        lines.append(venues.zip_code)
        lines.append(venues.phone_num)
        lines.append(venues.web)
        lines.append(venues.email_address)
        lines.append(" ")

    for line in lines:
        textob.textLine(line)

    c.drawText(textob)
    c.showPage()
    c.save()
    buf.seek(0)

    return FileResponse(buf, as_attachment=True, filename='venue_file.pdf')


def venue_file_csv(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename=venue_file.csv'
    Venue = venue.objects.all()
    writer = csv.writer(response)
    writer.writerow(['Venue Name', 'Address', 'Zip Code', 'Phone', 'Web Address', 'Email'])
    for venues in Venue:
        writer.writerow(
            [venues.name, venues.address, venues.zip_code, venues.phone_num, venues.web, venues.email_address])
    return response


def venue_file_text(request):
    response = HttpResponse(content_type='text/plain')
    response['Content-Disposition'] = 'attachment; filename=venue_file.txt'
    Venue = venue.objects.all()
    lines = []
    for venues in Venue:
        lines.append(
            f'{venues.name}\n{venues.address}\n{venues.zip_code}\n{venues.phone_num}\n{venues.web}\n{venues.email_address}\n\n')
    response.writelines(lines)
    return response


def delete_event(request, event_id):
    event = Event.objects.get(id=event_id)
    event.delete()
    return redirect('list-events')


def delete_venue(request, venue_id):
    Venue = venue.objects.get(id=venue_id)
    Venue.delete()
    return redirect('list-venue')


def search_venue(request):
    if request.method == "POST":
        searched = request.POST["searched"]
        venues = venue.objects.filter(name__contains=searched)
        return render(request, "search_venue.html", {"searched": searched, "venue": venues})
    else:
        return render(request, "search_venue.html", {})


def add_event(request):
    submitted = False
    if request.method == "POST":
        form = event_form(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/add_event?submitted=True")
    else:
        form = event_form
        if "submitted" in request.GET:
            submitted = True
    return render(request, 'add_event.html', {'form': form, 'submitted': submitted})


def add_venue(request):
    submitted = False
    if request.method == 'POST':
        form = venue_form(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/add_venue?submitted=True")

    else:
        form = venue_form
        if "submitted" in request.GET:
            submitted = True
    return render(request, "venueform.html", {"form": form, "submitted": submitted})


def update_event(request, event_id):
    event = Event.objects.get(id=event_id)
    ev_form = event_form(request.POST or None, instance=event)
    if ev_form.is_valid():
        ev_form.save()
        return redirect('list-events')

    return render(request, "update_event.html", {"event": event, "event_form": ev_form})


def update(request, venue_id):
    Venue = venue.objects.get(id=venue_id)
    form = venue_form(request.POST or None, instance=Venue)
    if form.is_valid():
        form.save()
        return redirect('list-venue')

    return render(request, "updated.html", {"venue": Venue, "form": form})


def show_venue(request, venue_id):
    Venue = venue.objects.get(id=venue_id)
    return render(request, "show_venues.html", {"venue": Venue})


def all_venues(request):
    venues_list = venue.objects.all().order_by('name')
    return render(request, "venue.html", {"venues_list": venues_list})


def all_events(request):
    events_list = Event.objects.all().order_by('name')
    return render(request, "events.html", {"events_list": events_list})


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
