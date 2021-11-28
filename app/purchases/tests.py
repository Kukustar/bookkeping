from django.test import TestCase
from .serializers import *
from .models import *
from .views import *


class PurchaseTests(TestCase):
    general_balance = 229

    def setUp(self):
        Balance.objects.create(mount=self.general_balance)
        PurchaseType.objects.create(title="Beer", code=1)

    def test_check_balance(self):
        balance = Balance.objects.get(id=1)
        purchase = PurchaseType.objects.get(id=1)
        self.assertEqual(balance.mount, self.general_balance)
        self.assertEqual(purchase.title, 'Beer')

    def test_add_purchase(self):
        purchase_amount = 100
        volume = {"amount": purchase_amount, "date": "2021-11-22 20:52", "title": "Beer"}
        serializer = PurchasesSerializer.create(self, validated_data=volume)
        balance = Balance.objects.get(id=1)
        self.assertEqual(balance.mount, self.general_balance - purchase_amount)

    def test_two_purchases(self):
        first_purchase_amount = 100
        second_purchase_amount = 123
        payload_fist_purchase = {"amount": first_purchase_amount, "date": "2021-11-22 20:52", "title": "Beer"}
        payload_two_purchase = {"amount": second_purchase_amount, "date": "2021-11-22 20:52", "title": "Snacks"}

        PurchasesSerializer.create(self, validated_data=payload_fist_purchase)
        PurchasesSerializer.create(self, validated_data=payload_two_purchase)
        balance_after_two_purchases_transaction = Balance.objects.get(id=1)
        expected_balance_after_two_purchases = self.general_balance - first_purchase_amount - second_purchase_amount

        self.assertEqual(balance_after_two_purchases_transaction.mount, expected_balance_after_two_purchases)

        PurchaseViewSet.perform_destroy(self, Purchase.objects.get(id=2))
        expected_balance_after_first_purchase = self.general_balance - first_purchase_amount
        balance_after_one_purchases_transaction = Balance.objects.get(id=1)

        self.assertEqual(balance_after_one_purchases_transaction.mount, expected_balance_after_first_purchase,
                         'test that after delete second purchase balance equal ...')

    def test_changing_purchase(self):
        second_purchase = 100
        first_purchase = 10
        first_volume = {"amount": first_purchase, "date": "2021-11-23 18:00", "title": "Beer"}
        second_volume = {"amount": second_purchase, "date": "2021-11-23 18:00", "title": "Beer"}
        PurchasesSerializer.create(self, validated_data=first_volume)
        PurchasesSerializer.create(self, validated_data=second_volume)

        balance_after_two_purchase = Balance.objects.get(id=1)
        self.assertEqual(balance_after_two_purchase.mount, self.general_balance - first_purchase - second_purchase)

        PurchaseViewSet.perform_destroy(self, Purchase.objects.get(id=1))
        balance_after_delete_first_purchase = Balance.objects.get(id=1)
        self.assertEqual(balance_after_delete_first_purchase.mount, self.general_balance - second_purchase)


class DepositeTest(TestCase):
    general_balance = 229

    def setUp(self):
        Balance.objects.create(mount=self.general_balance)

    def test_add_deposite(self):
        deposite_amount = 1000
        volume = {"date": "2021-11-22 21:26", "amount": deposite_amount, "title": "Salary"}
        serializer = DepositSerializer.create(self, validated_data=volume)
        deposite = Balance.objects.get(id=1)
        self.assertEqual(deposite.mount, self.general_balance + deposite_amount)

    def test_change_deposite(self):
        deposite_amount = 1000
        changed_deposit_amount = 1200
        first_volume = {"date": "2021-11-22 21:26", "amount": deposite_amount, "title": "Salary"}
        second_volume = {"date": "2021-11-23 20:26", "amount": changed_deposit_amount, "title": "Salary with some extra"}
        DepositSerializer.create(self, validated_data=first_volume)
        DepositSerializer.create(self, validated_data=second_volume)
        balance = Balance.objects.get(id=1)
        self.assertEqual(balance.mount, self.general_balance + deposite_amount + changed_deposit_amount,
                         ' сравниваю полученный баланс и 2 внесенных депозита')

        DepositViewSet.perform_destroy(self, Deposit.objects.get(id=1))
        balance_after_first_volume_delete = Balance.objects.get(id=1)
        self.assertEqual(balance_after_first_volume_delete.mount, self.general_balance + changed_deposit_amount, 'сравниваю баланс со вторым депозитом, после удалнеия первого')

