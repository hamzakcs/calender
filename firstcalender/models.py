from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class venue(models.Model):
    name = models.CharField('Venue name', max_length=120)
    address = models.CharField('Address', max_length=300)
    zip_code = models.CharField('Zip Code', max_length=15)
    phone_num = models.CharField('Phone Number', max_length=20, blank=True)
    web = models.URLField("Website Address", blank=True)
    email_address = models.EmailField('Email Address', blank=True)


    def __str__(self):
        return self.name


class CODEClubUser(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField('User Email', blank=True)

    def __str__(self):
        return self.first_name + ' ' + self.last_name


class Event(models.Model):
    name = models.CharField('Event_name', max_length=100)
    event_date = models.DateTimeField('Event_date')
    venue = models.ForeignKey(venue, blank=True, null=True, on_delete=models.CASCADE)
    manager = models.ForeignKey(User, default=True, blank=True, null=True, on_delete=models.SET_NULL)
    description = models.TextField(blank=True)
    attendees = models.ManyToManyField(CODEClubUser, blank=True)

    def __str__(self):
        return self.name
