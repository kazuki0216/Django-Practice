from django.urls import include, path
from rest_framework.routers import SimpleRouter

from .customer import views

router = SimpleRouter(trailing_slash=False)
router.register(r"customers", views.CustomerView, basename="customer")


urlpatterns = [
    path("", include(router.urls)),
    path("api-auth/", include("rest_framework.urls", namespace="rest_framework")),
]
