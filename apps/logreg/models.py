from django.db import models
import re
import bcrypt


class UserManager(models.Manager):
    def reg_validator(self, form):
        errors = {}
        if not form['name']:
            errors['name'] = 'Name cannot be blank'
        elif len(form['name']) < 3:
            errors['name'] = 'Name must be at least three characters'
        if not form['username']:
            errors['username'] = 'Username cannot be blank'
        elif len(form['username']) < 3:
            errors['username'] = 'Username must be at least three characters'
        else:
            users = User.objects.filter(username=form['username'])
            if users:
                errors['username'] = "User is already in database"
        if not form['password']:
            errors['password'] = 'Password cannot be blank'
        elif len(form['password']) < 8:
            errors['password'] = 'Password must be atleast eight characters'
        if form['confirm_password'] != form['password']:
            errors['confirm_password'] = 'Passwords do not match!'
        return errors

    def login_validator(self, form):
        errors = {}
        if not form['pwd']:
            errors['pwd'] = 'Password cannot be blank'
        if not form['username']:
            errors['login_username'] = 'Username cannot be blank'
        else:
            users = User.objects.filter(username=form['username'])
            if not users:
                errors['login_username'] = 'This username doesnt exist. Please register!'
            elif not bcrypt.checkpw(form['pwd'].encode(), users[0].hashpw.encode()):
                errors['pwd'] = 'Wrong password'
            return errors
        return errors


class User(models.Model):
    name = models.CharField(max_length=255)
    username = models.CharField(max_length=255)
    hashpw = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()
