from django.contrib import admin

from .customer import customer
from .menu import menu
from .order import order
from .payment import payment
from .subscription import subscription

# Register your models here.
admin.site.register(customer.Customer)
admin.site.register(subscription.Subscription)
admin.site.register(order.Order)
admin.site.register(menu.Menu)
admin.site.register(payment.Payment)
