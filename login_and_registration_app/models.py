from django.db import models
import re

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

class UserManager(models.Manager):
    def register_validator(self, postData):
        errors={}
        if len(postData['first_name']) < 2:
            errors['first_name'] = 'First name must be at least 2 characters'
        if len(postData['last_name']) < 2:
            errors['last_name'] = 'Last name must be at least 2 characters'
        email=User.objects.filter(email=postData['email'])
        if len(email) > 0:
            errors['email'] = 'This email already exists'
        elif len(postData['email']) < 0:
            errors['email'] = 'Email is required'
        elif not EMAIL_REGEX.match(postData['email']):
            errors['email'] = 'Invalid Email address'
        if len(postData['password']) < 4:
            errors['password'] = 'Password must be at least 4 characters'
        elif postData['password'] != postData['confirm_pw']:
            errors['password'] = 'Passwords must match'
        return errors

class User(models.Model):
    first_name=models.CharField(max_length=255)
    last_name=models.CharField(max_length=255)
    email=models.EmailField(max_length=255)
    password=models.CharField(max_length=255)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    objects=UserManager()

