import datetime

from django.db import models

from usuarios.models.kind import Kind


class Team(models.Model):
    description = models.CharField(max_length=50)
    kind_id = models.OneToOneField(
        Kind,
        on_delete=models.CASCADE,
        primary_key=True,
    )
    active = models.BooleanField(default=True)
    company_id = models.OneToOneField(
        Company,
        on_delete=models.CASCADE,
        primary_key=True,
    )
    workflow_id = models.OneToOneField(
        Workflow,
        on_delete=models.CASCADE,
        primary_key=True,
    )
    create_at = models.DateTimeField(auto_now_add=True, blank=True)
    updated_at = models.DateTimeField(default=datetime.datetime.now(), blank=True)

