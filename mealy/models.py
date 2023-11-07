from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
from django.conf import settings
from django.contrib.auth.models import User

# Guest - Movie - Resrvation


class Movie(models.Model):
    hall = models.CharField(max_length=20)
    movie = models.CharField(max_length=50)
    date = models.DateField(max_length=15)


class Guest(models.Model):
    name = models.CharField(max_length=20)
    mobile_num = models.CharField(max_length=20)


class Reservation(models.Model):
    guest = models.ForeignKey(
        Guest, related_name="reservation", on_delete=models.CASCADE
    )
    movie = models.ForeignKey(
        Movie, related_name="reservation", on_delete=models.CASCADE
    )


class post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=30)
    body=models.TextField(max_length=30)

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def Token_create(sender, instance, created, **kwargs):
    if created:
        Token.objects.create(user=instance)
