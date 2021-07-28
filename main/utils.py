from django.db.models import Count
from .models import *

menu = [{'title': 'О сайте', 'url_name': 'about_us'},
        {'title': 'Добавить товар', 'url_name': 'add_page'},
        {'title': 'Обратная связь', 'url_name': 'contact'}]


class DataMixin:
    paginate_by = 2

    def get_user_context(self, **kwargs):
        context = kwargs
        cats = Category.objects.annotate(Count('notebook'))
        user_menu = menu.copy()
        if not self.request.user.is_authenticated:
            user_menu.pop(1)
        context['menu'] = user_menu
        context['cats'] = cats
        if 'cat_selected' not in context:
            context['cat_selected'] = 0
        return context

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title=self.title)
        return dict(list(context.items()) + list(c_def.items()))
