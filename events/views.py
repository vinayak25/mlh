from django.shortcuts import render
from events.forms import EventForm


def create_tech_event(request):
    form = EventForm()

    return render(request, "new_event.html", {'form': form})
