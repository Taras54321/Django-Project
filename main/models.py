from django.db import models
from django.urls import reverse


class Notebook(models.Model):
    objects = '__all__'
    title = models.CharField(max_length=255, verbose_name='Название')
    content = models.TextField(blank=True, verbose_name='Описание')
    photo = models.ImageField(upload_to='photos', verbose_name='Фото')
    # time_create = models.DateTimeField(auto_now_add=True, verbose_name='Время добавления')
    price = models.CharField(max_length=20, verbose_name='Цена')
    in_stock = models.BooleanField(default=True, verbose_name='В наличии')
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name='URL')
    cat = models.ForeignKey('Category', on_delete=models.PROTECT, verbose_name='Категория')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post', kwargs={'post_slug': self.slug})

    class Meta:
        verbose_name = 'Ноутбук'
        verbose_name_plural = 'Ноутбуки'
        ordering = ['price', 'title']


class Category(models.Model):
    objects = '__all__'
    name = models.CharField(max_length=100, db_index=True, verbose_name='Процессор')
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name='URL')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('category', kwargs={'cat_slug': self.slug})

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ['id']
