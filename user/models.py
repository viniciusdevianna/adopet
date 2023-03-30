from django.db import models
from django.contrib.auth.models import User

class BrazilState(models.Model):
    short_name = models.CharField(max_length=2, primary_key=True)
    full_name = models.CharField(max_length=100)

class Profile(models.Model):
    user = models.OneToOneField(User, related_name='profile', on_delete=models.CASCADE)
    phone = models.CharField(max_length=12, blank=True)
    city = models.CharField(max_length=100)
    state = models.ForeignKey(BrazilState, related_name='estado', on_delete=models.DO_NOTHING)
    about = models.CharField(max_length=480, blank=True)
    is_tutor = models.BooleanField(default=False)

