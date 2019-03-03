import datetime

from django.db import models

from usuarios.model.workflow import Workflow


class Kanban(models.Model):
    name = models.CharField(max_length=30)
    workflow_id = models.ForeignKey(Workflow, on_delete=models.CASCADE)
    description = models.CharField(max_length=100)
    active = models.BooleanField(default=True)
    create_at = models.DateTimeField(auto_now_add=True, blank=True)
    updated_at = models.DateTimeField(default=datetime.datetime.now(), blank=True)

    def __str__(self):
        return self.name
