from django.db import models

class PurchaseType(models.Model):
    title = models.CharField(max_length=200)
    code = models.CharField(max_length=200)
    description = models.CharField(blank=True, max_length=200)

class Transaction(models.Model):
    amount = models.FloatField(default=0.0)
    title = models.CharField(max_length=200)
    description = models.CharField(blank=True, max_length=200)

    class Meta:
        abstract = True

class Purchase(Transaction):
    date = models.DateTimeField('purchase date time')
    type = models.ForeignKey(PurchaseType, default=1, on_delete=models.PROTECT)

class Deposit(Transaction):
    date = models.DateTimeField('deposit date time')

class Balance(models.Model):
    mount = models.FloatField(default=0.0)
    name = models.CharField(blank=True, max_length=200)

    def top_up_balance(self, mount):
        self.mount = self.mount + mount
        self.save()

    def reduce_the_balance(self, mount):
        self.mount = self.mount - mount
        self.save()


