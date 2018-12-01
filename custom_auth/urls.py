from django.contrib import admin
from django.urls import path, include
from custom_auth import views

urlpatterns = [
<<<<<<< HEAD
    path('login/', views.login_view, name="login"),
    path('attendee-register/', views.register_view_attendee,
         name="register_attendee"),
    path('organiser-register/', views.register_view_organiser,
         name="register_organiser"),
    path('sponsor-register/', views.register_view_sponsor,
         name="register_sponsor"),
    path('profile/', views.profile, name="profile"),
=======
    path('login/', views.login_view),
    path('attendee-register/', views.register_view_attendee),
    path('organiser-register/', views.register_view_organiser),
    path('sponsor-register/', views.register_view_sponsor),
    path('profile/', views.profile),
    path('logout/', views.logout_view, name='logout'),
>>>>>>> f5da3c7aba9ba664fdf98a4f698079547436561e
]
