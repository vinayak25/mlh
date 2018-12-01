from django.shortcuts import render, redirect
from events.forms import EventForm
from events.models import Event
from django.contrib.auth.decorators import login_required


@login_required(login_url='/custom_auth/login')
def create_tech_event(request):
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


@login_required(login_url='/custom_auth/login')
def create_hack_event(request):
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
