from django.shortcuts import render, redirect
from custom_auth.forms import LoginForm,RegisterForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User

# Create your views here.
def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            user = authenticate(username = username, password = password)
            if user is not None:
                login(request, user)
                return render(request, 'profile.html')
            else:
                return redirect('/attendee-register/')
    else:
        form = LoginForm()
        return render(request, 'login.html', {'form':form})

def register_view(request):
    if request.method == 'POST':
            form = RegisterForm(request.POST)
            if form.is_valid():
                username = form.cleaned_data['username']
                password = form.cleaned_data['password']
                user = User.objects.create_user(username=username,password=password)
    return render(request ,'register.html',{'form':form})