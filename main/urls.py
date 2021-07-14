from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='home'),
    path('about_us', views.about_us, name='about_us'),
    path('create', views.create, name='create'),
    path('registration', views.registration, name='registration'),
    path('login', views.login, name='login'),
]
