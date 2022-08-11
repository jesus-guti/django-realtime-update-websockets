from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils.text import slugify

class Notification(models.Model):
    text = models.CharField(max_length=200)