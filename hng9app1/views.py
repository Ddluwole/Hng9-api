from multiprocessing import context
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.http import JsonResponse
import json

# Create your views here.

# @api_view(['GET'])
# def hngapi(request):
#     cont = {
#         "slackUsername": "ddluwole",
#         "backend": True,
#         "age": 21,
#         "bio": "I play table tennis and code",
#     }
#     resp= Response(cont)
#     resp["Access-Control-Allow-Origin"] = "*"
#     return resp


@api_view(['POST'])
def operation(request):
    x = request.data['x']
    y = request.data['y']
    # x = request.json.get('x')
    # y = request.json.get('y')
    

    if type(x) and type(y) == int:
        operation_type = request.data['operation_type']
        # operation_type = request.json.get('operation_type')
        if operation_type == 'addition':
            result = x + y
        elif operation_type == 'subtraction':
            result = x - y
        elif operation_type == 'multiplication':
            result = x * y
    else:
        result = 'Invalid operation or data type'
    cont = {
        "slackUsername": "ddluwole",
        "result": result,
        "operation_type": operation_type,
    }
    resp= Response(cont)
    resp["Access-Control-Allow-Origin"] = "*"
    return resp




