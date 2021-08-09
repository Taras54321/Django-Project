# Generated by Django 3.2 on 2021-08-06 09:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=100, verbose_name='Процессор')),
                ('slug', models.SlugField(max_length=255, unique=True, verbose_name='URL')),
            ],
            options={
                'verbose_name': 'Категория',
                'verbose_name_plural': 'Категории',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Notebook',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Название')),
                ('content', models.TextField(blank=True, verbose_name='Описание')),
                ('photo', models.ImageField(upload_to='photos', verbose_name='Фото')),
                ('price', models.CharField(max_length=20, verbose_name='Цена')),
                ('in_stock', models.BooleanField(default=True, verbose_name='В наличии')),
                ('slug', models.SlugField(max_length=255, unique=True, verbose_name='URL')),
                ('cat', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='main.category', verbose_name='Категория')),
            ],
            options={
                'verbose_name': 'Ноутбук',
                'verbose_name_plural': 'Ноутбуки',
                'ordering': ['title', 'price'],
            },
        ),
    ]
