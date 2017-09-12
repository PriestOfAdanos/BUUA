from django import forms
from .models import Order
from .custom_user_model import User
from django.contrib.auth.forms import UserCreationForm


class NewBasket(forms.ModelForm):
    class Meta:
        model = Order
        fields = ('pickup_time',)
        labels = {'pickup_time': 'Godzina odbioru'}
