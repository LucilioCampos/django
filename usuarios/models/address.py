import datetime

from django.db import models


class Address(models.Model):
    state = models.CharField(max_length=2)
    city = models.CharField(max_length=20)
    address = models.TextField
    number = models.CharField(max_length=5)
    details = models.CharField(max_length=100)
    create_at = models.DateTimeField(auto_now_add=True, blank=True)
    updated_at = models.DateTimeField(default=datetime.datetime.now(), blank=True)
