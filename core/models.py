from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):

    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255, unique=True)
    password = models.CharField(max_length=255)
    username = None

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

class Class(models.Model):

    name = models.CharField(max_length=255)
    description = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
class Currency(models.Model):
    
    name = models.CharField(max_length=255)
    exchange = models.FloatField()
    fee_percentage = models.FloatField()
    quantity = models.FloatField()

class TrackFee(models.Model):
    
    fee_amount = models.FloatField()
    date_transaction = models.CharField(max_length=255)
    base_currency = models.ForeignKey(
        Currency, on_delete=models.SET_NULL, null=True, related_name='base')
    quote_currency = models.ForeignKey(
        Currency, on_delete=models.SET_NULL, null=True, related_name='quote')
    
    
