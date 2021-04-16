import requests
from rest_framework.decorators import api_view
from .crawler import get_articles, eth_price, address_value
from rest_framework.response import Response
from rest_framework import status


# Create your views here.

@api_view(['GET'])
def crypto_articles(request):
    return Response({'articles' : get_articles()})

@api_view(['GET'])
def ethereum_price(request):
    return Response({'price' :eth_price()})

@api_view(['GET'])
def ethereum_wallet_value(request, address):
    return Response({'value' : address_value(address)}) 