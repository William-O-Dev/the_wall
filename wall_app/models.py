from django.db import models
from login_and_registration_app.models import User
from django.db.models.fields.related import ForeignKey


class Message(models.Model):
    message=models.TextField()
    user=models.ForeignKey(User, related_name='messages', on_delete=models.CASCADE)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

class Comment(models.Model):
    comment=models.TextField()
    user=models.ForeignKey(User, related_name='comments', on_delete=models.CASCADE)
    message=models.ForeignKey(Message, related_name='comments', on_delete=models.CASCADE)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
