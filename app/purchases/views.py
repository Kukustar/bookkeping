from rest_framework import viewsets
from rest_framework import permissions
from .serializers import PurchasesSerializer
from .models import Purchase

class PurchaseViewSet(viewsets.ModelViewSet):
    queryset = Purchase.objects.all()
    serializer_class = PurchasesSerializer
    permission_classes = [permissions.IsAuthenticated]

