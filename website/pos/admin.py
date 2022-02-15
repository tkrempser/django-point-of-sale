from django.contrib import admin

from pos.models import Customer, Product, Order, OrderProduct


admin.site.register(Customer)
admin.site.register(Product)
admin.site.register(Order)
admin.site.register(OrderProduct)
