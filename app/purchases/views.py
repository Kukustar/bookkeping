from rest_framework import viewsets
from rest_framework import permissions
from .serializers import PurchasesSerializer, BalanceSerializer, DepositSerializer
from .models import Purchase, Balance, Deposit

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
