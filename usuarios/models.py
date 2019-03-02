import datetime

from django.db import models

from usuarios.models.address import Address
from usuarios.models.kind import Kind
from usuarios.models.license import License
from usuarios.models.team import Team


class Usuario(models.Model):
    username = models.CharField(max_length=30)
    password = models.CharField(max_length=20)
    name = models.CharField(max_length=30)
    email = models.CharField(max_length=30)
    address = models.OneToOneField(
        Address,
        on_delete=models.CASCADE,
        primary_key=True,
    )
    phone = models.CharField(max_length=20)
    active = models.BooleanField(default=True)
    create_at = models.DateTimeField(auto_now_add=True, blank=True)
    updated_at = models.DateTimeField(default=datetime.datetime.now(), blank=True)
    license_id = models.ForeignKey(License, on_delete=models.CASCADE)
    team_id = models.ForeignKey(Team, on_delete=models.CASCADE)



