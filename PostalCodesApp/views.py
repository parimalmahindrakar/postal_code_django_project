from django.shortcuts import render, HttpResponse
from django.http import JsonResponse
from .models import *
import json
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def getCode(request,code_):
    code_ = PostalCodes.objects.filter(code=code_)
    data = {'data':{}}
    for i in code_:
        data['data'].update({i.area:i.code})
    if len(code_) == 0:
        return JsonResponse({"data":"NO"})
    else:
        return JsonResponse(data)
