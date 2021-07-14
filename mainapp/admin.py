from django.contrib import admin
from .models import Product,Category,CustomerModel,OrderModel

# Register your models here.
admin.site.register(Product)
admin.site.register(Category)
admin.site.register(CustomerModel)
admin.site.register(OrderModel)