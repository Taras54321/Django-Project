from .models import Task, Registration, Login
from django import forms
from django.contrib.auth.models import User
# from django.forms import ModelForm, TextInput, Textarea


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'task']
        widgets = {'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Введите название'}),
                   'task': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Введите описание'})}


class RegistrationForm(forms.ModelForm):
    class Meta:
        model = Registration
        fields = ['username', 'password']
        widgets = {'username': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Введите логин'}),
                   'password': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Введите пароль'})}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].label = 'Логин'
        self.fields['password'].label = 'Пароль'

    def clean(self):
        username = self.cleaned_data['username']
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError(f'Логин {username} уже занят. Придумайте другой логин')
        return self.cleaned_data


class LoginForm(forms.ModelForm):
    class Meta:
        model = Login
        fields = ['username', 'password']
        widgets = {'username': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Введите логин'}),
                   'password': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Введите пароль'})}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].label = 'Логин'
        self.fields['password'].label = 'Пароль'

    def clean(self):
        username = self.cleaned_data['username']
        password = self.cleaned_data['password']
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError(f'Пользователь с логином {username} не найден')
        user = User.objects.filter(username=username).first()
        if user:
            if not user.check_password(password):
                raise forms.ValidationError('Неверный пароль')
        return self.cleaned_data
