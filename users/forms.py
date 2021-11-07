from django import forms
from .models import User
from django.contrib.auth.forms import AuthenticationForm


class UserLoginForm(AuthenticationForm):
    class_name = 'form-control mb-2'
    username = forms.CharField(max_length=50,
                            required= True,
                            label="Имя пользователя",
                            widget=forms.TextInput(
                                attrs={'class': class_name}))

    password = forms.CharField(label="Пароль",
                                widget=forms.PasswordInput(
                                    attrs={'class': class_name})
                                )
    class Meta:
        model = User
        field = ('username', 'password')
