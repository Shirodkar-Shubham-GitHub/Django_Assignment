from django.db import models
from django.utils.timezone import now

class DemoModel(models.Model):
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(default=now)

    def __str__(self):
        return self.name
