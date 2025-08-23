from django.db import DatabaseError

from ..schema.customer import CustomerCreateRequest
from .customer import Customer


def insert_new_customer(information: CustomerCreateRequest):
    try:
        new_customer = Customer.objects.create(
            name=information.name,
            email=information.email,
            phone_number=information.phone_number,
        )
        new_customer.save()
    except DatabaseError as e:
        raise e


def get_customer_info(name, email):
    try:
        find_customer = Customer.objects.get(name=name, email=email)
        return find_customer
    except DatabaseError as e:
        raise e
