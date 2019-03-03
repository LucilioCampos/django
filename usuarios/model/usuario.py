import datetime

from django.db import models

from .license import License
from .team import Team


class Usuario(models.Model):

    username = models.CharField(max_length=30)
    password = models.CharField(max_length=20)
    name = models.CharField(max_length=30)
    email = models.CharField(max_length=30)
    phone = models.CharField(max_length=20)
    active = models.BooleanField(default=True)
    create_at = models.DateTimeField(auto_now_add=True, blank=True)
    updated_at = models.DateTimeField(default=datetime.datetime.now(), blank=True)
    license_id = models.ForeignKey(License, on_delete=models.CASCADE, default=0)
    team_id = models.ForeignKey(Team, on_delete=models.CASCADE, default=0)

    def __str__(self):
        return self.name


    class Meta:
        app_label = "usuarios"
        abstract = True
