from django.db import models


class Sauna(models.Model):
    last_chair_person = models.IntegerField(default=0)