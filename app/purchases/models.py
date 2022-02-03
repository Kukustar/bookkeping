from django.db.models import Sum
from django.db import models
from datetime import datetime, timedelta
from calendar import monthrange

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

    @staticmethod
    def get_last_day_purchase_sum():
        yesterday_start = datetime.today().replace(hour=0, minute=0, second=0, microsecond=0) - timedelta(days = 1 )
        yesterday_end = datetime.today().replace(hour=23, minute=59, second=59, microsecond=0) - timedelta(days = 1 )
        amount_sum_yesterday = Purchase.objects.filter(date__range=(yesterday_start, yesterday_end)).aggregate(Sum('amount'))

        return amount_sum_yesterday

    @staticmethod
    def get_today_purchase_sum():
        day_start = datetime.today().replace(hour=0, minute=0, second=0, microsecond=0)
        day_end = datetime.today()
        amount_today = Purchase.objects.filter(date__range=(day_start, day_end)).aggregate(Sum('amount'))

        return amount_today

    # TODO this func is more for balance model 
    @staticmethod
    def get_available_for_day_balance():
        [_, days_in_month] = monthrange(datetime.now().year, datetime.now().month)
        days_before_month_end = days_in_month - datetime.now().day
        total_balance = Balance.objects.get(id=1)

        return round(total_balance.mount / days_before_month_end, 1)


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


