from django.urls import path
from . import views
from .views import NotebookHome, NotebookCategory, ShowPost, AddPage

urlpatterns = [
    path('', NotebookHome.as_view(), name='home'),
    path('about_us', views.about_us, name='about_us'),
    path('add_page', AddPage.as_view(), name='add_page'),
    path('contact', views.contact, name='contact'),
    path('login', views.login, name='login'),
    path('post/<slug:post_slug>', ShowPost.as_view(), name='post'),
    path('category/<slug:cat_slug>', NotebookCategory.as_view(), name='category'),
]
