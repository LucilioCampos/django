from django.db import models


class License(models.Model):
    name = models.CharField(max_length=20)

