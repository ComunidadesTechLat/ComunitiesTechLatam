
# Django
from django.http import HttpResponse
from django.shortcuts import render
## utilities
from datetime import datetime

def home(request):
    context = {
        'latest_community': "Comunity LAST Python",
    }
    return render(request, 'web/home.html', context)

def about(request):
    return HttpResponse('About')

def community(request, id):
    return HttpResponse('Community {}'.format(id))