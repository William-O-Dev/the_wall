from django.shortcuts import render, redirect
from login_and_registration_app.models import *
from .models import *

def wall_index(request):
    if 'user_id' not in request.session:
        return redirect('/')
    context = {
        'messages': Message.objects.all(),
    }
    return render(request, 'wall_index.html', context)

def add_messages(request):
    message = Message.objects.create(
        message=request.POST['message'],
        user=User.objects.get(id=request.session['user_id'])
    )
    return redirect('/wall')

def add_comments(request, message_id):
    user = User.objects.get(id=request.session['user_id'])
    message = Message.objects.get(id=message_id)
    comment = Comment.objects.create(
        comment=request.POST['comment'],
        message=message,
        user=user
    )
    return redirect('/wall')
