from django.urls import path
from .views import ethereum_info

urlpatterns = [
    path('eth-info', ethereum_info, name='eth_info')
]