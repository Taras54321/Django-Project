from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseNotFound, HttpResponse
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView
from .models import Notebook
from .forms import AddPostForm

menu = [{'title': 'О сайте', 'url_name': 'about_us'},
        {'title': 'Добавить товар', 'url_name': 'add_page'},
        {'title': 'Обратная связь', 'url_name': 'contact'},
        {'title': 'Войти', 'url_name': 'login'}]


class NotebookHome(ListView):
    model = Notebook
    template_name = 'main/index.html'
    context_object_name = 'notebooks'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu'] = menu
        context['title'] = 'Главная страница'
        context['cat_selected'] = 0
        return context

    def get_queryset(self):
        return Notebook.objects.filter(in_stock=True)


def about_us(request):
    return render(request, 'main/about_us.html')


class AddPage(CreateView):
    form_class = AddPostForm
    template_name = 'main/addpage.html'
    success_url = reverse_lazy('home')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu'] = menu
        context['title'] = 'Добавление товара'
        return context

# def add_page(request):
#    if request.method == 'POST':
#        form = AddPostForm(request.POST, request.FILES)
#        if form.is_valid():
#            form.save()
#            return redirect('home')
#    else:
#        form = AddPostForm()
#    return render(request, 'main/addpage.html', {'form': form, 'menu': menu, 'title': 'Добавление товара'})


def contact(request):
    return HttpResponse('Обратная связь')


def login(request):
    return HttpResponse('Авторизация')


class ShowPost(DetailView):
    model = Notebook
    template_name = 'main/post.html'
    slug_url_kwarg = 'post_slug'
    context_object_name = 'post'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu'] = menu
        context['title'] = context['post']
        return context


# def show_post(request, post_slug):
#    post = get_object_or_404(Notebook, slug=post_slug)
#    context = {'post': post,
#               'menu': menu,
#               'title': post.title,
#               'cat_selected': post.cat_id,
#               }
#    return render(request, 'main/post.html', context=context)


class NotebookCategory(ListView):
    model = Notebook
    template_name = 'main/index.html'
    context_object_name = 'notebooks'
    allow_empty = False

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu'] = menu
        context['title'] = 'Категория - ' + str(context['notebooks'][0].cat)
        context['cat_selected'] = context['notebooks'][0].cat_id
        return context

    def get_queryset(self):
        return Notebook.objects.filter(cat__slug=self.kwargs['cat_slug'], in_stock=True)


def page_not_found(request, response):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')
