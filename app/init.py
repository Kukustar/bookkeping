from purchases.models import *

if Balance.objects.count() == 0:
    balance = Balance(name='General')
    balance.save()

if PurchaseType.objects.count() == 0:
    purchaseType = q = PurchaseType(title='default', code='')
    purchaseType.save()


