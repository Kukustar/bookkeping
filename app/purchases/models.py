from django.db import models

class Purchase(models.Model):
    date = models.DateTimeField('purchase date time')
    cost = models.FloatField(default=0.0)
    title = models.CharField(max_length=200)
    description = models.CharField(blank=True, max_length=200)

class Balance(models.Model):
    mount = models.FloatField(default=0.0)
    name = models.CharField(blank=True, max_length=200)

    def top_up_balance(self, mount):
        self.mount = self.mount + mount
        self.save()

    def reduce_the_balance(self, mount):
        self.mount = self.mount - mount
        self.save()

class Deposit(models.Model):
    date = models.DateTimeField('deposit date time')
    amount = models.FloatField(default=0.0)
    title = models.CharField(max_length=200)
    description = models.CharField(blank=True, max_length=200)
