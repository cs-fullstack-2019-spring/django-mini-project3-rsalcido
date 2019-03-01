from django.db import models
from datetime import date
from django. utils import timezone

# Time Card Model
class TimeCardModel(models.Model):

    name = models.CharField(max_length=50, default='')
    school = models.CharField(max_length=50, default='')
    subject = models.CharField(max_length=50, default='')
    hours = models.DecimalField(max_digits=4, decimal_places=2)
    dow = models.DateField(default=date.today())
    entryDate = models.DateTimeField(default=timezone.now())

    def __str__(self):
        return self.timecard



