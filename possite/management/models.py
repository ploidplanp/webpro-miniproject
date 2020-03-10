from tokenize import Double
from django.db import models

# Create your models here.
class Type(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return '%s' % (self.name)

class Product(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20)
    type = models.ForeignKey(Type, on_delete=models.CASCADE)
    description = models.TextField(null=True, blank=True)
    price = models.FloatField(default=0.00)

    def __str__(self):
        return '%s ; %s (%.2f)' % (self.name, self.type.name, self.price)