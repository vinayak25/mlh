from django.contrib import admin
from django.urls import path, include
from events import views

urlpatterns = [
    path('new-tech/', views.create_tech_event, name='new_tech_event'),
    path('new-hack/', views.create_hack_event, name='new_hack_event'),
    path('<int:event_id>/attend-event/', views.mark_event_attendee, name='attend-event'),
]
