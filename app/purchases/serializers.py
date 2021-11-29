from .models import Purchase, Balance, Deposit, PurchaseType
from rest_framework import serializers

class PurchaseTypeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = PurchaseType
        fields = ['title', 'code', 'id']

class PurchasesSerializer(serializers.HyperlinkedModelSerializer):
    type = PurchaseTypeSerializer(required=False, read_only=True)
    type_id = serializers.PrimaryKeyRelatedField(
        required=False, queryset=PurchaseType.objects.all(), source='type', allow_null=True
    )

    class Meta:
        model = Purchase
        fields = ['date', 'amount', 'title', 'description', 'id', 'type_id', 'type']

    def create(self, validated_data):
        total_balance = Balance.objects.get(id=1)
        total_balance.reduce_the_balance(validated_data["amount"])

        return Purchase.objects.create(**validated_data)



class BalanceSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Balance
        fields = ['name', 'mount']
        read_only_fields = ['name', 'mount']

class DepositSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Deposit
        fields = ['date', 'amount', 'title', 'description', 'id']

    def create(self, validated_data):
        total_balance = Balance.objects.get(id=1)
        total_balance.top_up_balance(validated_data["amount"])

        return Deposit.objects.create(**validated_data)