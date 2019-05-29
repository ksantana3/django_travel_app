from django.shortcuts import render, HttpResponse, redirect
from ..logreg.models import User
from .models import *
from django.contrib import messages


def dashboard(request):
    print("Logged In")
    print(request.session['id'])
    person = User.objects.get(id=request.session['id'])
    user = User.objects.get(id=request.session['id'])
    context = {
        'trips': Trip.objects.filter(trip_members=person),
        'other_trips': Trip.objects.all().exclude(trip_members=person),
        'user': user,
    }
    return render(request, "travel_app/travel.html", context)


def destination(request, travel_id):
    context = {
        'trip': Trip.objects.get(id=travel_id),
        'planner': User.objects.get(id=(Trip.objects.get(id=travel_id).created_by_id)).name,
        'others': User.objects.filter(joined_trips=travel_id).exclude(id=(Trip.objects.get(id=travel_id).created_by_id))
    }
    return render(request, "travel_app/destination.html", context)


def add(request):

    return render(request, "travel_app/add.html")


def process_trip(request):
    errors = Trip.objects.trip_validator(request.POST)
    if errors:
        for key, value in errors.items():
            messages.add_message(request, messages.ERROR, value, key)
        return redirect("/travel/add")
    print(request.POST['userid'])
    print(request.POST['description'])
    trip = Trip.objects.create(destination=request.POST['destination'], plan=request.POST['description'], start_date=request.POST['date_from'], end_date=request.POST['date_to'], created_by=User.objects.get(id=request.session['id']))
    return redirect("/travel")


def join(request, travel_id):
    user = User.objects.get(id=request.session['id'])
    trip = Trip.objects.get(id=travel_id)
    trip.trip_members.add(user)
    trip.save()
    return redirect('/travel')
