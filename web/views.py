# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import datetime
from json import JSONEncoder
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from web.models import Token, Income, User, Expense


@csrf_exempt
def submit_expense(request):
    # TODO : validate data
    print(request.POST)
    token = request.POST['token']
    user = User.objects.filter(token__token=token).get()
    Expense.objects.create(text=request.POST['text'], date=datetime.datetime.now(), amount=request.POST['amount'],
                           user=user)
    return JsonResponse({
        "status": "ok"
    }, encoder=JSONEncoder)
