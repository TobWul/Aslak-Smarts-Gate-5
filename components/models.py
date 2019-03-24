from django.db import models

TYPES = [
        ('light', 'light'),
        ('socket', 'socket')
    ]


class Component(models.Model):
    ikea_id = models.PositiveIntegerField()
    name = models.CharField(max_length=300)
    type = models.CharField(max_length=100, choices=TYPES)
    state = models.BooleanField()

    def __str__(self):
        return self.name
