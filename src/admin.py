from django.contrib import admin

from .models import Customer, Menu, Order, Payment, Subscription

# Register your models here.
admin.site.register(Customer)
admin.site.register(Subscription)
admin.site.register(Order)
admin.site.register(Menu)
admin.site.register(Payment)
