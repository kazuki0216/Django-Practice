from django.urls import path

from . import views

urlpatterns = [
    path("azure", views.azure_index, name="azure_index"),
    path("claude", views.claude_index, name="claude_index"),
]