from django.shortcuts import render, redirect
from .models import User
from django.contrib import messages
import bcrypt

def index(request):
    return render(request, 'index.html')

def register(request):
    pw_hash=bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt()).decode()
    errors=User.objects.register_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect ('/')
    else:
        user = User.objects.create(
            first_name=request.POST['first_name'],
            last_name=request.POST['last_name'],
            email=request.POST['email'],
            password=pw_hash,
        )
        request.session['user_id']=user.id
        request.session['user_first_name']=user.first_name
        request.session['user_last_name']=user.last_name
        return redirect('/wall')

def authenticate(request):
    user = User.objects.filter(email=request.POST['email'])
    if user:
        logged_user=user[0]
        if bcrypt.checkpw(request.POST['password'].encode(), logged_user.password.encode()):
            request.session['user_id']=logged_user.id
            request.session['user_first_name']=logged_user.first_name
            request.session['user_last_name']=logged_user.last_name
            return redirect('/wall')
        else:
            messages.error(request, "Incorrect email and/or password.")
            return redirect('/')

# def success(request):
#     if 'user_id' not in request.session:
#         return redirect('/')
#     user = User.objects.get(id=request.session['user_id'])
#     context = {
#         'user':user
#     }
#     return render(request, 'success.html', context)

def logout(request):
    request.session.flush()
    return redirect('/')

