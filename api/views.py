import requests
from rest_framework.decorators import api_view
from .crawler import get_articles
from rest_framework.response import Response


# Create your views here.



@api_view(['GET'])
def ethereum_info(request):
    return Response({'articles' : get_articles()})

