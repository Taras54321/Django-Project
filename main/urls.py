from django.urls import path
from . import views
from .views import *

urlpatterns = [
    path('', NotebookHome.as_view(), name='home'),
    path('about_us/', views.about_us, name='about_us'),
    path('add_page/', AddPage.as_view(), name='add_page'),
    path('contact/', views.contact, name='contact'),
    path('login/', LoginUser.as_view(), name='login'),
    path('logout/', logout_user, name='logout'),
    path('register/', RegisterUser.as_view(), name='register'),
    path('post/<slug:post_slug>/', ShowPost.as_view(), name='post'),
    path('category/<slug:cat_slug>/', NotebookCategory.as_view(), name='category'),
]
