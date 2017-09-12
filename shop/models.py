from __future__ import unicode_literals
from django.contrib.auth.models import BaseUserManager
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.core.mail import send_mail
from django.utils.translation import ugettext_lazy as _
import datetime
# import custom_user_model


now = datetime.datetime.now().strftime('%H:%M')  #  Time like '23:12'



class Product(models.Model):
    """
    Creates a product taht user can add to order
    """
    name = models.CharField(max_length=100)
    photo = models.ImageField(upload_to='hot_rolls_pics', max_length=100)
    desc = models.TextField()

    def __str__(self):
        return self.name


class Section(models.Model):
    """
    Section of products in shop
    """
    name = models.CharField(max_length=200)
    product = models.ForeignKey(Product, related_name='section')
    pic = models.ImageField(upload_to='section_themes', max_length=100)


class Order(models.Model):
    """
    Order with list of products & pickup date. Is passed to execute
    """
    products = models.ForeignKey(Product, related_name='history_of_orders')
    user = models.ForeignKey(User)
    pickup_time = models.TimeField(default=now)
    comments = models.CharField(max_length=200, blank=True)


