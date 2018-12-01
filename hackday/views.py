from django.shortcuts import render, redirect


def root(request):
    if request.user is not None:
        if request.user.is_authenticated:
            return redirect("/custom_auth/profile")
    return render(request, "index.html")
