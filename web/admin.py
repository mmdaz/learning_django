# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .models import Expense, Income, Token
from django.contrib import admin

# Register your models here
admin.site.register(Expense)
admin.site.register(Income)
admin.site.register(Token)