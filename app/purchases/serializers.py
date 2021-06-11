from .models import Purchase, Balance
from rest_framework import serializers


class PurchasesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Purchase
        fields = ['date', 'cost', 'title', 'description', 'id']

    def create(self, validated_data):
        total_balance = Balance.objects.get(id=1)
        total_balance.remove_mount_after_create(validated_data["cost"])

        return Purchase.objects.create(**validated_data)


class BalanceSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Balance
        fields = ['name', 'mount']