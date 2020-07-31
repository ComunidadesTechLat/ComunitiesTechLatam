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
                'name': '💻 PROGRAMACIÓN'
            },
            {
                'name': '🎨 DISEÑO | UI & UX'
            },
            {
                'name': '🔐 CIBERSEGURIDAD'
            },
            {
                'name': '💸 BLOCKCHAIN'
            },
            {
                'name': '🤖 IA | MACHINE LEARNING'
            },
            {
                'name': '📉 DATA SCIENCE'
            },
            {
                'name': '📊 MARKETING'
            },
            {
                'name': '👾 VIDEOJUEGOS'
            },
            {
                'name': '🚀 NEGOCIOS | EMPRENDIMIENTO'
            },
            {
                'name': '💼 EMPLEO | RH'
            },
            {
                'name': '📲 PRODUCTO '
            },
            {
                'name': '📷 AUDIOVISUAL'
            },
            {
                'name': '💎 NO CODE | LOW CODE'
            },
            {
                'name': ' 🔧 MAKERS'
            },
            {
                'name': '📈 TRADING'
            },
            {
                'name': '👩🏻‍💻 MUJERES'
            },
        ]
    }
    return render(request, 'web/events.html', context)

def contact(request):
    """Return HttpResponse of contact"""
    return render(request, 'web/contact.html')
