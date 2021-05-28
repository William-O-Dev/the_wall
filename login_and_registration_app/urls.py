from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('users/register', views.register),
    path('users/login', views.authenticate),
    # path('success', views.success),
    path('users/logout', views.logout),
]
