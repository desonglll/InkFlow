from django.http import JsonResponse
from django.shortcuts import render

from utils.data import Result


# Create your views here.

def hello_tips(request):
    user = request.user
    result = Result(200, f"hello {user}", None)
    return JsonResponse(result.to_json())
