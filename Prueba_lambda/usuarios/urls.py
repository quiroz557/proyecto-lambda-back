from django.urls import path
from .views import registro, login

urlpatterns = [
    path('registro/', registro),
    path('login/', login, name='login'),
    # otras URLs...
]
