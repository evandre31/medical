from django.contrib import messages
from django.contrib.auth.models import User
from django.shortcuts import render


def home(request):
    storage = messages.get_messages(request)
    users = User.objects.all()
    return render(request, 'home.html', {'users': users, 'messages': storage})

