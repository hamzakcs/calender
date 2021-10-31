from django import forms
from django.forms import ModelForm
from .models import venue, Event


class venue_form(ModelForm):
    class Meta:
        model = venue
        fields = ('name', 'address', 'zip_code', 'phone_num', 'web', 'email_address')
        labels = {
            "name": "",
            "address": "",
            "zip_code": "",
            "phone_num": "",
            "web": "",
            "email_address": "",
        }
        widgets = {
            "name": forms.TextInput(attrs={"class": "form-control", "placeholder": "Venue Name"}),
            "address": forms.TextInput(attrs={"class": "form-control", "placeholder": "Address"}),
            "zip_code": forms.TextInput(attrs={"class": "form-control", "placeholder": "Zip Code"}),
            "phone_num": forms.TextInput(attrs={"class": "form-control", "placeholder": "Phone Number"}),
            "web": forms.URLInput(attrs={"class": "form-control", "placeholder": "Website URL"}),
            "email_address": forms.EmailInput(attrs={"class": "form-control", "placeholder": "Email Address"}),

        }


class event_form(ModelForm):
    class Meta:
        model = Event
        fields = ('name', 'event_date', 'venue', 'manager', 'attendees', 'description')
        labels = {
            "name": "",
            "event_date": "YYY-MM-DD HH:MM:SS",
            "venue": "Venue",
            "manager": "Manager",
            "attendees": "",
            "description": "",
        }
        widgets = {
            "name": forms.TextInput(attrs={"class": "form-control", "placeholder": "Event Name"}),
            "event_date": forms.DateTimeInput(attrs={"class": "form-control", "placeholder": "Date"}),
            "venue": forms.Select(attrs={"class": "form-select", "placeholder": "------"}),
            "manager": forms.Select(attrs={"class": "form-select", "placeholder": "------"}),
            "attendees": forms.SelectMultiple(attrs={"class": "form-control"}),
            "description": forms.Textarea(attrs={"class": "form-control", "placeholder": "Description"}),

        }