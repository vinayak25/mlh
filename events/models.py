from django.db import models
import datetime
from django.contrib.auth.models import User


class Event(models.Model):
    name = models.CharField(max_length=255)
    type = models.IntegerField()
    date = models.DateField("Date", default=datetime.date.today)
    description = models.CharField(max_length=512)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    @property
    def event_type(self):
        if self.type == 1:
            return 'Tech Event'
        else:
            return 'Hackathon'
