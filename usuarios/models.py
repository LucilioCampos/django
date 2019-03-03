import datetime

from django.db import models


class Address(models.Model):
    #um para um endereco  pessoa
    usuario = models.OneToOneField(
        "Usuario",
        on_delete=models.CASCADE,
    )
    state = models.CharField(max_length=2)
    city = models.CharField(max_length=20)
    address = models.CharField(max_length=300)
    number = models.CharField(max_length=5)
    details = models.CharField(max_length=100)
    create_at = models.DateTimeField(default=datetime.datetime.now(), blank=True)
    updated_at = models.DateTimeField(default=datetime.datetime.now(), blank=True)

    def __str__(self):
        return self.address


class Usuario(models.Model):

    username = models.CharField(max_length=30)
    password = models.CharField(max_length=20)
    name = models.CharField(max_length=30)
    email = models.CharField(max_length=30)
    phone = models.CharField(max_length=20)
    active = models.BooleanField(default=True)
    create_at = models.DateTimeField(default=datetime.datetime.now(), blank=True)
    updated_at = models.DateTimeField(default=datetime.datetime.now(), blank=True)
    license = models.ForeignKey("License", on_delete=models.CASCADE, default=0)

    def __str__(self):
        return self.name


class Team(models.Model):
    name = models.CharField(max_length=50)
    user = models.ForeignKey("Usuario", on_delete=models.CASCADE)
    kind = models.OneToOneField(
        "Kind",
        on_delete=models.CASCADE,
    )
    active = models.BooleanField(default=True)
    company = models.OneToOneField(
        "Company",
        on_delete=models.CASCADE,
    )
    workflow = models.OneToOneField(
        "Workflow",
        on_delete=models.CASCADE,
    )
    create_at = models.DateTimeField(default=datetime.datetime.now(), blank=True)
    updated_at = models.DateTimeField(default=datetime.datetime.now(), blank=True)

    def __str__(self):
        return self.name


class Company(models.Model):
    name = models.CharField(max_length=100)
    address = models.ForeignKey("Address", on_delete=models.CASCADE)
    segment = models.CharField(max_length=30)
    owner = models.OneToOneField(
        "Usuario",
        on_delete=models.CASCADE,
    )
    description = models.TextField
    active = models.BooleanField(default=True)
    create_at = models.DateTimeField(default=datetime.datetime.now(), blank=True)
    updated_at = models.DateTimeField(default=datetime.datetime.now(), blank=True)

    def __str__(self):
        return self.name


class Kanban(models.Model):
    name = models.CharField(max_length=30)
    workflow = models.ForeignKey("Workflow", on_delete=models.CASCADE)
    description = models.CharField(max_length=100)
    active = models.BooleanField(default=True)
    create_at = models.DateTimeField(default=datetime.datetime.now(), blank=True)
    updated_at = models.DateTimeField(default=datetime.datetime.now(), blank=True)

    def __str__(self):
        return self.name


class License(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Workflow(models.Model):
    name = models.CharField(max_length=100)
    kind = models.OneToOneField(
        "Kind",
        on_delete=models.CASCADE,
    )
    active = models.BooleanField(default=True)
    create_at = models.DateTimeField(default=datetime.datetime.now(), blank=True)
    updated_at = models.DateTimeField(default=datetime.datetime.now(), blank=True)

    def __str__(self):
        return self.name


class Kind(models.Model):
    description = models.CharField(max_length=50)
    active = models.BooleanField(default=True)
    create_at = models.DateTimeField(default=datetime.datetime.now(), blank=True)
    updated_at = models.DateTimeField(default=datetime.datetime.now(), blank=True)

    def __str__(self):
        return self.description
