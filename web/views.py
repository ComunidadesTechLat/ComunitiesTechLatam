
# Django
from django.http import HttpResponse
from django.shortcuts import render
## utilities
from datetime import datetime

def home(request):

    return HttpResponse('HOME {now}'.format(
        now=datetime.now().strftime('%dth %m %Y')
        ))

def about(request):
    return HttpResponse('About')

def community(request, id):
    return HttpResponse('Community {}'.format(id))