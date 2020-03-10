from django.db import models
from management.models import Product

# Create your models here.
class Order(models.Model):
    id = models.AutoField(primary_key=True)
    date_time = models.DateField(auto_now=False, auto_now_add=False)
    total_price = models.IntegerField(default=0.00)

    def __str__(self):
        return 'Order: %03d (%.2f ฿)' %(self.id, self.total_price)
    

class Order_Products(models.Model):
    id = models.AutoField(primary_key=True)
    order_id = models.ForeignKey(Order, on_delete=models.CASCADE)
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    amount = models.IntegerField(default=0)

    def __str__(self):
        return 'Order: %03d' %self.id
    