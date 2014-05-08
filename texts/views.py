from django.shortcuts import render
from django.http import HttpResponse

from .models import Text

import datetime
import time
import json
# Create your views here.


def hello(request):
    return HttpResponse('<html><h1>%s</h1></html>' % 'Hello World')


def texts_list(request):
    modifier = request.GET.get('modifier', 'lower')
    texts = list(Text.objects.all().values_list('name', flat=True))
    result = json.dumps(texts)

    if modifier == 'upper':
        result = result.upper()
    elif modifier == 'lower':
        result = result.lower()
    return HttpResponse(result)


def texts_detail(request, text_id=None):
    return HttpResponse('<html><h1>Texto #%s</h1></html>' % text_id)
