from django.contrib import admin

# Register your models here.
from .models import Purchase, PurchaseType

@admin.register(Purchase)
class PurchaseAdmin(admin.ModelAdmin):
    list_display = ["view_date", "view_amount", "title", "type"]
    list_filter = ["date"]

    @admin.display()
    def view_date(self, obj):
        return obj.date.strftime("%H:%M %d.%m.%Y")

    @admin.display()
    def view_amount(self, obj):
        return str(obj.amount) + ' ₽'



@admin.register(PurchaseType)
class PurchaseTypeAdmin(admin.ModelAdmin):
    list_display = ["id", "title"]