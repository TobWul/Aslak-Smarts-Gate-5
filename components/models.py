from django.db import models

TYPES = [
        ('light', 'light'),
        ('outlet', 'outlet')
    ]


class Component(models.Model):
    name = models.CharField(max_length=300)
    type = models.CharField(max_length=100, choices=TYPES)
    state = models.BooleanField()

    def __str__(self):
        return self.name
