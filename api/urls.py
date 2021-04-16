from django.urls import path
from .views import crypto_articles, ethereum_price, ethereum_wallet_value

urlpatterns = [
    path('crypto-news', crypto_articles, name='news'),
    path('eth-price', ethereum_price, name='price'),
    path('wallet', ethereum_wallet_value, name='value'),
]