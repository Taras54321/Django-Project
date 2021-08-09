from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from captcha.fields import CaptchaField
from .models import Category


class AddPostForm(forms.Form):
    title = forms.CharField(label='Название', max_length=255, widget=forms.TextInput(attrs={'class': 'form-input'}))
    slug = forms.SlugField(label='URL', max_length=255)
    content = forms.CharField(label='Описание', widget=forms.Textarea(attrs={'cols': 60, 'rows': 10}))
    photo = forms.ImageField(label='Фото')
    in_stock = forms.BooleanField(label='В наличии')
    cat = forms.ChoiceField(label='Категория', choices=Category.objects.values_list('id', 'name'))
    price = forms.CharField(label='Цена', max_length=20)

    def clean_title(self):
        title = self.cleaned_data['title']
        if len(title) > 200:
            raise ValidationError('Длина превышает 200 символов')
        return title


class RegisterUserForm(UserCreationForm):
    username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={'class': 'form-input'}))
    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-input'}))
    password2 = forms.CharField(label='Повтор пароля', widget=forms.PasswordInput(attrs={'class': 'form-input'}))

    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']


class LoginUserForm(AuthenticationForm):
    username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={'class': 'form-input'}))
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-input'}))


class ContactForm(forms.Form):
    name = forms.CharField(label='Имя', widget=forms.TextInput(attrs={'class': 'form-input'}))
    email = forms.EmailField(label='Email', widget=forms.TextInput(attrs={'class': 'form-input'}))
    content = forms.CharField(label='Содержание', widget=forms.Textarea(attrs={'cols': 60, 'rows': 10}))
    captcha = CaptchaField()


class SellingForm(forms.Form):
    DELIVERY_METHODS = (('1', 'Самовывоз'),
                        ('2', 'Нова Пошта'),
                        ('3', 'Укрпошта'),
                        ('4', 'Курьером по адресу'))
    PAYMENT_METHODS = (('1', 'Оплата при получении товара'),
                       ('2', 'Картой онлайн'),
                       ('3', 'Безналичная оплата'))
    first_name = forms.CharField(label='Ваше имя', widget=forms.TextInput(attrs={'class': 'form-input'}))
    last_name = forms.CharField(label='Ваша фамилия', widget=forms.TextInput(attrs={'class': 'form-input'}))
    address = forms.CharField(label='Ваш адрес', widget=forms.Textarea(attrs={'cols': 60, 'rows': 2}))
    delivery_method = forms.ChoiceField(label='Способ доставки', choices=DELIVERY_METHODS)
    payment_method = forms.ChoiceField(label='Способ оплаты', choices=PAYMENT_METHODS)
    content = forms.CharField(label='Пожелания', widget=forms.Textarea(attrs={'cols': 60, 'rows': 10}))
