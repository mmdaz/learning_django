# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import json
from json import JSONEncoder
from django.http import JsonResponse
from django.shortcuts import render


# Create your views here.

def submit_expense(request):
    print(request.POST)

    return JsonResponse({
        "status": "ok"
    }, encoder=JSONEncoder)