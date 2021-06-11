from rest_framework import viewsets
from rest_framework import permissions
from .serializers import PurchasesSerializer, BalanceSerializer
from .models import Purchase, Balance

class PurchaseViewSet(viewsets.ModelViewSet):
    queryset = Purchase.objects.all().order_by('-date')
    serializer_class = PurchasesSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_destroy(self, instance):
        total_balance = Balance.objects.get(id=1)
        total_balance.return_mount_after_delete(getattr(instance, 'cost'))
        instance.delete()


class BalanceViewSet(viewsets.ModelViewSet):
    queryset = Balance.objects.all()
    serializer_class = BalanceSerializer
    permission_classes = [permissions.IsAuthenticated]