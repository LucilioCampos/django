import datetime

from django.db import models

from usuarios.model.address import Address
from usuarios.model.usuario import Usuario


class Company(models.Model):
    name = models.CharField(max_length=100)
    address = models.ForeignKey(Address, on_delete=models.CASCADE)
    segment = models.CharField(max_length=30)
    owner = models.OneToOneField(
        Usuario,
        on_delete=models.CASCADE,
        primary_key=True
    )
    description = models.TextField
    active = models.BooleanField(default=True)
    create_at = models.DateTimeField(auto_now_add=True, blank=True)
    updated_at = models.DateTimeField(default=datetime.datetime.now(), blank=True)

    def __str__(self):
        return self.name


    class Meta:
        app_label = "usuarios"
        abstract = True
