from django.contrib import admin
from django.urls import path, include
from custom_auth import views

urlpatterns = [
    path('login/', views.login_view),
    path('attendee-register/', views.register_view_attendee),
    path('organiser-register/', views.register_view_organiser),
    path('sponsor-register/', views.register_view_sponsor),
    path('profile/', views.profile),
    path('logout/', views.logout_view, name='logout'),
]
