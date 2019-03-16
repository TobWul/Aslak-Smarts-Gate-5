from django.db import models


class Electricity(models.Model):
    month = models.PositiveIntegerField()
    year = models.PositiveIntegerField()
    grid_cost = models.PositiveIntegerField()
    electricity_cost = models.PositiveIntegerField()
    sum = models.PositiveIntegerField(blank=True, null=True)

    def __str__(self):
        month = '0' + str(self.month)
        return month[-2:] + '.' + str(self.year)

    def save(self, *args, **kwargs):
        if self.grid_cost and self.electricity_cost:
            self.sum = self.grid_cost + self.electricity_cost
        super(Electricity, self).save(*args, **kwargs)
