from django.contrib import admin

from .models import customer, subscription, order, menu, payment

# Register your models here.
admin.site.register(customer.Customer)
admin.site.register(subscription.Subscription)
admin.site.register(order.Order)
admin.site.register(menu.Menu)
admin.site.register(payment.Payment)