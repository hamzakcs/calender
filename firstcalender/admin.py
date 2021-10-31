from django.contrib import admin
from .models import Event
from .models import CODEClubUser
from .models import venue

# Register your models here.
# admin.site.register(Event)
admin.site.register(CODEClubUser)


# admin.site.register(venue)
@admin.register(venue)
class venue_admin(admin.ModelAdmin):
    list_display = ('name', 'address', 'phone_num')
    ordering = ('name',)
    search_fields = ('name', 'address', 'phone_num')


@admin.register(Event)
class event_admin(admin.ModelAdmin):
    fields = ('name', 'venue', 'event_date', 'description', 'manager')
    list_display = ('name', 'event_date', 'venue')
    list_filter = ('event_date', 'venue')
    ordering = ('-event_date',)
