from django.contrib import admin

from .models import Customer, Subscription, Order, MenuItem, Payment

# Register your models here.
admin.site.register(Customer)
admin.site.register(Subscription)
admin.site.register(Order)
admin.site.register(MenuItem)
admin.site.register(Payment)