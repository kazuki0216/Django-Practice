from django.urls import path

from . import views

urlpatterns = [
    path("menu", views.cafe_menu, name="cafe_menu"),
    path("order", views.order, name="order"),
]
