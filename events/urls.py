from django.contrib import admin
from django.urls import path, include
from events import views

urlpatterns = [
    path('new-tech/', views.create_tech_event),
    path('new-hack/', views.create_hack_event)
]
