from django.db import models


class Task(models.Model):
    title = models.CharField('Название', max_length=100)
    task = models.TextField('Описание')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Задача'
        verbose_name_plural = 'Задачи'


class Registration(models.Model):
    username = models.CharField('Логин', max_length=50)
    password = models.CharField('Пароль', max_length=50)

    class Meta:
        verbose_name = 'Регистрация'


class Login(models.Model):
    username = models.CharField('Логин', max_length=50)
    password = models.CharField('Пароль', max_length=50)

    class Meta:
        verbose_name = 'Вход'
