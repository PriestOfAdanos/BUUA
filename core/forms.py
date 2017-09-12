from django import forms
from .custom_user_model import User
from django.contrib.auth.forms import UserCreationForm


class CreateUser(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'password',)

