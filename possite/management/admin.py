from codecs import register

from django.contrib import admin

from management.models import Product, Type


class ProductInline(admin.StackedInline):
    model = Product
    extra = 1

class productAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'description', 'type', 'description']
    list_per_page = 10
    
    #ใส่ชื่อใน model ที่เราต้องการจะ filter
    list_filter = ['price', 'type']
    search_fields = ['name']
    list_per_page = 10

    fieldsets = [
        (None, {'fields': ['name', 'type', 'price']}),
        ('Description', {'fields': ['description'], 'classes': ['collapse']})
    ]

class typeAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'description']
    search_fields = ['name']
    list_per_page = 10

    inlines = [ProductInline]


# Register your models here.
admin.site.register(Type, typeAdmin)
admin.site.register(Product, productAdmin)