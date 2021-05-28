from django.urls import path, include

urlpatterns = [
    path('', include('login_and_registration_app.urls')),
    path('wall', include('wall_app.urls')),
]
