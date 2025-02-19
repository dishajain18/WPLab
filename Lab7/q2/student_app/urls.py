from django.urls import path
from . import views

urlpatterns = [
    path('', views.first_page, name='first_page'),  # First page URL
    path('second/', views.second_page, name='second_page'),  # Second page URL
]
