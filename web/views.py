"""This a baisic view module."""
# Django
from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    """Return template home"""
    context = {
        'latest_community': "Comunity LAST Python",
    }
    return render(request, 'web/home.html', context)

def about():
    """Return HttpResponse about"""
    return HttpResponse('About')

def community(request, id):
    # pylint: disable=W0612,W0622,W0613,C0103
    """Return tHttpResponse with a param"""
    return HttpResponse('Community {}'.format(id))
