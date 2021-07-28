from django.contrib.auth import logout, login
from django.contrib.auth.views import LoginView
from django.shortcuts import redirect
from django.http import HttpResponseNotFound
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, FormView
from django.contrib.auth.mixins import LoginRequiredMixin

from .forms import AddPostForm, RegisterUserForm, LoginUserForm, ContactForm
from .utils import *


class NotebookHome(DataMixin, ListView):
    template_name = 'main/index.html'
    context_object_name = 'notebooks'
    title = 'Главная страница'

    def get_queryset(self):
        return Notebook.objects.filter(in_stock=True).select_related('cat')


class AddPage(LoginRequiredMixin, DataMixin, FormView):
    form_class = AddPostForm
    template_name = 'main/addpage.html'
    success_url = reverse_lazy('home')
    login_url = reverse_lazy('home')
    raise_exception = True
    title = 'Добавление товара'


class ShowPost(DataMixin, DetailView):
    model = Notebook
    template_name = 'main/post.html'
    slug_url_kwarg = 'post_slug'
    context_object_name = 'post'
    title = Notebook.objects.filter()


class NotebookCategory(DataMixin, ListView):
    # model = Category
    template_name = 'main/index.html'
    context_object_name = 'notebooks'
    allow_empty = False
    title = 'Категория - ' + str(Category.objects.filter())

    def get_queryset(self):
        return Notebook.objects.filter(cat__slug=self.kwargs['cat_slug'],
                                       in_stock=True).select_related('cat')


class RegisterUser(DataMixin, CreateView):
    form_class = RegisterUserForm
    template_name = 'main/register.html'
    success_url = reverse_lazy('login')
    title = 'Регистрация'

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('home')


class LoginUser(DataMixin, LoginView):
    form_class = LoginUserForm
    template_name = 'main/login.html'
    title = 'Авторизация'

    def get_success_url(self):
        return reverse_lazy('home')


class ContactFormView(DataMixin, FormView):
    form_class = ContactForm
    template_name = 'main/contact.html'
    success_url = reverse_lazy('home')
    title = 'Обратная связь'

    def form_valid(self, form):
        print(form.cleaned_data)
        return redirect('home')


class AboutUsView(DataMixin, ListView):
    model = Notebook
    paginate_by = None
    template_name = 'main/about_us.html'
    title = 'О сайте'


def logout_user(request):
    logout(request)
    return redirect('login')


def page_not_found(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')
