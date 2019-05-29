from django.db import models
from apps.logreg.models import User
from datetime import datetime, time, date
from time import strftime


class tripManager(models.Manager):
    def trip_validator(self, postData):
        errors = {}
        d = datetime.now()
        now = d.strftime("%Y-%m-%d")
        if len(postData['destination']) < 3:
            errors['destination'] = 'Destination must be at least three characters'
        if len(postData['description']) < 10:
            errors['description'] = 'Description must be at least ten characters'
        if len(postData['date_from']) < 10:
            errors['date_from'] = "Starting travel date must be entered"
        if len(postData['date_to']) < 10:
            errors['date_to'] = "Ending travel date must be entered"
        if postData['date_to'] < postData['date_from']:
            errors['date_to'] = "Starting date must be before ending date"
        if postData['date_from'] < now:
            errors['date_from'] = "Starting date must be in the future"
        return errors


class Trip(models.Model):
    destination = models.CharField(max_length=100)
    plan = models.CharField(max_length=255)
    start_date = models.DateField()
    end_date = models.DateField()
    created_by = models.ForeignKey(User, related_name="created_trips", on_delete=models.CASCADE)
    trip_members = models.ManyToManyField(User, related_name="joined_trips")
    updated_at = models.DateTimeField(auto_now=True)
    objects = tripManager()
