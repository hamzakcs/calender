from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('<int:year>/<str:month>/', views.home, name='home'),
    path('eventcard/', views.all_events, name='list-events'),
    path('add_venue/', views.add_venue, name='add-venue'),
    path('venuecard/', views.all_venues, name='list-venue'),
    path('show_venue/<venue_id>', views.show_venue, name='show-venue'),
    path('search_venue/', views.search_venue, name='search-venue'),
    path('update/<venue_id>/', views.update, name='update-venue'),
    path('event_update/<event_id>/', views.update_event, name='update-event'),
    path('add_event/', views.add_event, name='add-event'),
    path('delete_event/<event_id>/', views.delete_event, name='delete-event'),
    path('delete_venue?<venue_id>/', views.delete_venue, name='delete-venue'),
    path('venue_file_text/', views.venue_file_text, name='venue-file-text'),
    path('venue_file_csv/', views.venue_file_csv, name='venue-file-csv'),
    path('venue_file_pdf/', views.venue_file_pdf, name='venue-file-pdf'),
]
