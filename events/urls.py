from django.contrib import admin
from django.urls import path, include
from events import views

urlpatterns = [
    path('new-tech/', views.create_tech_event, name='new_tech_event'),
    path('new-hack/', views.create_hack_event, name='new_hack_event'),
    path('<int:event_id>/attend-event/', views.mark_event_attendee, name='attend-event'),
    path('tech-events/', views.get_tech_events, name='get_tech_events'),
    path('hackathons/', views.get_hackathons, name='get_hackathons'),
    path('<int:event_id>/sponsor', views.sponsor_event, name='sponsor-event')
]
