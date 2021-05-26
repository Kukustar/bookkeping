from .models import Purchase
from rest_framework import serializers


class PurchasesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Purchase
        fields = ['date', 'cost', 'title', 'description', 'id']