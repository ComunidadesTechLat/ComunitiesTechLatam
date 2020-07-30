"""This a baisic view module."""
# Django
from django.shortcuts import render

def home(request):
    """Return template home"""
    context = {
        'latest_community': "Comunity LAST Python",
        'latest_uuid': "28445554-d109-11ea-87d0-0242ac130003"
    }
    return render(request, 'web/home.html', context)

def about(request):
    """Return HttpResponse of about"""
    return render(request, 'web/about.html')

def community(request, id):
    """Return template community details"""
    # pylint: disable=W0622,C0103
    context = {
        'id': id
    }
    return render(request, 'web/community.html', context)

def events(request):
    """Return HttpResponse of event"""
    context = {
        'categories': [
            {
                'name': 'Interface'
            },
            {
                'name': 'Devops'
            },
            {
                'name': 'UI/UX'
            },
            {
                'name': 'Javascript'
            },
        ]
    }
    return render(request, 'web/events.html', context)

def contact(request):
    """Return HttpResponse of contact"""
    return render(request, 'web/contact.html')
