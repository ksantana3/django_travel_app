from django.shortcuts import render, redirect
import bcrypt
from django.contrib import messages
from .models import *


def index(request):

    return render(request, "logreg/logreg.html")


def register(request):
    errors = User.objects.reg_validator(request.POST)
    if errors:
        for key, value in errors.items():
            messages.add_message(request, messages.ERROR, value, key)
        return redirect("/")
    password_hash = bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt())
    user = User.objects.create(name=request.POST['name'], username=request.POST['username'], hashpw=password_hash.decode())
    request.session['id'] = user.id
    return redirect("/travel")


def login(request):
    errors = User.objects.login_validator(request.POST)
    if errors:
        for key, value in errors.items():
            messages.add_message(request, messages.ERROR, value, key)
        return redirect("/")
    else:
        users = User.objects.filter(username=request.POST['username'])
        request.session['id'] = users[0].id
    return redirect("/success")


def success(request):
    if 'id' in request.session:
        return redirect('/travel')
    else:
        return redirect('/')


def logout(request):
    request.session.clear()
    return redirect('/')
