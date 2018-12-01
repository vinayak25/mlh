from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Role(models.Model):
    name = models.CharField(max_length=255)
    permission = models.ManyToManyField("Permission")
    user = models.ManyToManyField(User)
    def __str__(self):
        return self.name


class Permission(models.Model):
    name = models.CharField(max_length=255)

