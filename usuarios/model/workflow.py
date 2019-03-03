import datetime

from django.db import models

from usuarios.model.kind import Kind


class Workflow(models.Model):
    name = models.CharField(max_length=100)
    kind_id = models.OneToOneField(
        Kind,
        on_delete=models.CASCADE,
        primary_key=True
    )
    active = models.BooleanField(default=True)
    create_at = models.DateTimeField(auto_now_add=True, blank=True)
    updated_at = models.DateTimeField(default=datetime.datetime.now(), blank=True)

    def __str__(self):
        return self.name
