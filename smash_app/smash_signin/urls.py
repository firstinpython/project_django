from django.urls import path
from .views import loggin,profile
app_name = 'user'
urlpatterns = [
    path('login/',loggin, name="login"),
    path('profile/',profile, name = "profile" )
]