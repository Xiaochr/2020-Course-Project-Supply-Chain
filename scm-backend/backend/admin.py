from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(MaterialInfo)
admin.site.register(MaterialStock)
admin.site.register(MaterialOrder)
admin.site.register(MaterialOrderDetail)
admin.site.register(KitchenOrder)
admin.site.register(KitchenOrderDetail)
