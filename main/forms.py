from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from captcha.fields import CaptchaField


class AddPostForm(forms.Form):
    CHOICES = (('0', 'Категория не выбрана'), ('1', 'AMD'), ('2', 'Intel'))
    title = forms.CharField(label='Название', max_length=255, widget=forms.TextInput(attrs={'class': 'form-input'}))
    slug = forms.SlugField(label='URL', max_length=255)
    content = forms.CharField(label='Описание', widget=forms.Textarea(attrs={'cols': 60, 'rows': 10}))
    photo = forms.ImageField(label='Фото')
    in_stock = forms.BooleanField(label='В наличии')
    cat = forms.ChoiceField(label='Категория', choices=CHOICES)
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
    # email = forms.EmailField(label='Email', widget=forms.EmailInput(attrs={'class': 'form-input'}))

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
