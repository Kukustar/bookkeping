from django.db import models

class Purchase(models.Model):
    date = models.DateTimeField('purchase date time')
    cost = models.FloatField(default=0.0)
    title = models.CharField(max_length=200)
    description = models.CharField(blank=True, max_length=200)
