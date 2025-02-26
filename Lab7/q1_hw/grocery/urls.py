from django.urls import path
from .views import grocery_view

urlpatterns = [
    path('', grocery_view, name='grocery-list'),
]
