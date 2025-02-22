from django.db import models


class Appliance(models.Model):
    name = models.CharField(max_length=100)
    power = models.FloatField()
    is_active = models.BooleanField(default=False)

    def __str__(self):
        return self.name
