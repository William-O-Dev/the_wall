from django.urls import path
from . import views

urlpatterns = [
    path('', views.wall_index),
    path('/add_messages', views.add_messages),
    path('/add_comments/<int:message_id>', views.add_comments),

]