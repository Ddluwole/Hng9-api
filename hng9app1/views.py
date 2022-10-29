from multiprocessing import context
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.http import JsonResponse

# Create your views here.

# def Jsonviews(request):
#     cont = {
#         "slackUsername": "David",
#         "backend": True,
#         "age": 21,
#         "bio": "I play table tennis and code",
#     }
    
#     return JsonResponse(cont)

@api_view(['GET'])
def hngapi(request):
    cont = {
        "slackUsername": "ddluwole",
        "backend": True,
        "age": 21,
        "bio": "I play table tennis and code",
    }
    return Response(cont)
