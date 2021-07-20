from datetime import datetime, timedelta
from django.db.models import Sum


from rest_framework import viewsets
from rest_framework import permissions
from rest_framework.views import APIView

from .serializers import PurchasesSerializer, BalanceSerializer, \
    DepositSerializer, PurchaseTypeSerializer
from .models import Purchase, Balance, Deposit, PurchaseType

from rest_framework.response import Response



class PurchaseViewSet(viewsets.ModelViewSet):
    queryset = Purchase.objects.all().order_by('-date')
    serializer_class = PurchasesSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_destroy(self, instance):
        total_balance = Balance.objects.get(id=1)
        total_balance.top_up_balance(getattr(instance, 'amount'))
        instance.delete()


class BalanceViewSet(viewsets.ModelViewSet):
    queryset = Balance.objects.all()
    serializer_class = BalanceSerializer
    permission_classes = [permissions.IsAuthenticated]

class DepositViewSet(viewsets.ModelViewSet):
    queryset = Deposit.objects.all().order_by('-date')
    serializer_class = DepositSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_destroy(self, instance):
        total_balance = Balance.objects.get(id=1)
        total_balance.reduce_the_balance(getattr(instance, 'amount'))
        instance.delete()


class PurchaseTypeViewSet(viewsets.ModelViewSet):
    queryset = PurchaseType.objects.all()
    serializer_class = PurchaseTypeSerializer
    permission_classes = [permissions.IsAuthenticated]


class StatisticViewSet(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, response):
        yesterday_start = datetime.today().replace(hour=0, minute=0, second=0, microsecond=0) - timedelta(days = 1 )
        yesterday_end = datetime.today().replace(hour=23, minute=59, second=59, microsecond=0) - timedelta(days = 1 )
        data = Purchase.objects.filter(date__range=(yesterday_start, yesterday_end)).aggregate(Sum('amount'))

        return Response({ 'last-day': data['amount__sum'] })
