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
        last_day = Purchase.get_last_day_purchase_sum()
        today = Purchase.get_today_purchase_sum()

        return Response({
            'last-day': last_day['amount__sum'],
            'today': today['amount__sum']
        })


class DayBalanceViewSet(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, response):
        availabe_for_day = Purchase.get_available_for_day_balance()

        return Response({
            'availabe_for_day': availabe_for_day
        })