from django.urls import path
from . import views

urlpatterns = [
    path('', views.register_view, name='register'),
    path('success/', views.success_view, name='success'),
]
