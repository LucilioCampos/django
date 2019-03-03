import datetime

from django.db import models


class Kind(models.Model):
    description = models.CharField(max_length=50)
    active =  models.BooleanField(default=True)
    create_at = models.DateTimeField(auto_now_add=True, blank=True)
    updated_at = models.DateTimeField(default=datetime.datetime.now(), blank=True)

    def __str__(self):
        return self.description
