from django import template
from main.models import *

register = template.Library()


@register.simple_tag(name='getcats')
def get_categories(filter1=None):
    if not filter1:
        return Category.objects.all()
    else:
        return Category.objects.filter(pk=filter1)


@register.inclusion_tag('main/list_categories.html')
def show_categories(sort=None, cat_selected=0):
    if not sort:
        cats = Category.objects.all()
    else:
        cats = Category.objects.order_by(sort)
    return {'cats': cats, 'cat_selected': cat_selected}
