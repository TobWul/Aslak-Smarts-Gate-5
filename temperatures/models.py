from django.db import models


class InsideTemperature(models.Model):
    timestamp = models.DateTimeField()
    temperature = models.FloatField()

    def __str__(self):
        return str(self.temperature)
