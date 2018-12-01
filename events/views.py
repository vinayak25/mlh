from django.shortcuts import render, redirect
from events.forms import EventForm
from events.models import Event
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404

@login_required(login_url='/custom_auth/login')
def create_tech_event(request):
    user = request.user
    if user.role_set.filter(id = 1):
        if request.method == 'POST':
            form = EventForm(request.POST)
            if form.is_valid():
                name = form.cleaned_data['name']
                description = form.cleaned_data['description']
                event_type = 1
                user_id = request.user.id
                date = form.cleaned_data['date']
                event = Event(user=request.user, name=name,
                            description=description, type=event_type, date=date)
                event.save()
                return redirect('http://127.0.0.1:8000/custom_auth/profile/')
            else:
                return render(request, 'new_event.html', {'form': form})
        else:
            form = EventForm()
            return render(request, "new_event.html", {'form': form})
    else:
        return render(request, 'not_permitted.html')

@login_required(login_url='/custom_auth/login')
def create_hack_event(request):
    user = request.user
    if user.role_set.filter(id = 1):
        if request.method == 'POST':
            form = EventForm(request.POST)
            if form.is_valid():
                name = form.cleaned_data['name']
                description = form.cleaned_data['description']
                event_type = 2
                user_id = request.user.id
                date = form.cleaned_data['date']
                event = Event(user=request.user, name=name,
                            description=description, type=event_type, date=date)
                event.save()
                return redirect('http://127.0.0.1:8000/custom_auth/profile/')
            else:
                return render(request, 'new_event.html', {'form': form})
        else:
            form = EventForm()
            return render(request, "new_event.html", {'form': form})
    else:
        return render(request, 'not_permitted.html')

@login_required(login_url='/custom_auth/login')
def mark_event_attendee(request, event_id):
    user = request.user
    event = get_object_or_404(Event, pk=event_id)
    
    event.attendee.add(user)
    return redirect('http://127.0.0.1:8000/custom_auth/profile/')

@login_required(login_url='/custom_auth/login')
def get_tech_events(request):
    events = Event.objects.filter(type=1)
    return render(request, 'tech_events.html', { 'user': request.user, 'events': events })

@login_required(login_url='/custom_auth/login')
def get_hackathons(request):
    events = Event.objects.filter(type=2)
    return render(request, 'profile.html', { 'user': request.user, 'events': events })

@login_required(login_url='/custom_auth/login')
def sponsor_event(request, event_id):
    user = request.user
    event = get_object_or_404(Event, pk=event_id)
    event.sponsor.add(user)
    return redirect('http://127.0.0.1:8000/custom_auth/profile/')