from django.contrib import admin
from shop.models import Order, Order_Products

class Order_ProductInline(admin.StackedInline):
    model = Order_Products
    extra = 1

class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'date_time', 'total_price']
    list_filter = ['date_time', 'total_price']
    search_fields = ['date_time']
    list_per_page = 20

    inlines = [Order_ProductInline]


class Order_ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'order_id', 'product_id', 'amount']
    list_filter = ['product_id', 'amount']
    list_per_page = 10

# Register your models here.
admin.site.register(Order, OrderAdmin)
admin.site.register(Order_Products, Order_ProductAdmin)