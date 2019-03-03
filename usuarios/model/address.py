import datetime

from django.db import models

from usuarios.model.usuario import Usuario


class Address(models.Model):
    #um para um endereco  pessoa
    address = models.OneToOneField(
        Usuario,
        on_delete=models.CASCADE,
        primary_key=True,
    )
    state = models.CharField(max_length=2)
    city = models.CharField(max_length=20)
    address = models.TextField
    number = models.CharField(max_length=5)
    details = models.CharField(max_length=100)
    create_at = models.DateTimeField(auto_now_add=True, blank=True)
    updated_at = models.DateTimeField(default=datetime.datetime.now(), blank=True)

    def __str__(self):
        return self.address


    class Meta:
        app_label = "usuarios"
        abstract = True
