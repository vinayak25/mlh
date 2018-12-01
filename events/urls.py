from django.contrib import admin
from django.urls import path, include
from events import views

urlpatterns = [
    path('new/', views.create_tech_event),
]
