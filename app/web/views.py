# pylint: disable=E1101

"""This a basic view module."""
# Django
from django.shortcuts import render
# DB
from communities.models import Category, Community

def get_all_categories():
    """returns all avaliable categories"""
    return Category.objects.all()

def get_latest_community():
    """returns latest modified community"""
    return Community.objects.latest('modified')
def get_community_by_id(id):
    # pylint: disable=C0103,W0622
    """returns a community by a given id"""
    return Community.objects.get(id=id)

def home(request):
    """Return template home"""
    context = {
        'latest_community': get_latest_community(),
        'categories' : get_all_categories()
    }
    return render(request, 'web/home.html', context)

def about(request):
    """Return HttpResponse of about"""
    return render(request, 'web/about.html')

def community(request, id):
    """Return template community details"""
    # pylint: disable=W0622,C0103
    context = {
        'community':get_community_by_id(id)
    }
    return render(request, 'web/community.html', context)

def events(request):
    """Return HttpResponse of event"""
    context = {
        'categories' : get_all_categories()
    }
    return render(request, 'web/events.html', context)

def contact(request):
    """Return HttpResponse of contact"""
    return render(request, 'web/contact.html')

def filtered_communities(request, category):
    """Returns filtered communities by category"""
    if category == 'all':
        communities = Community.objects.filter(status='Active')
    else:
        category = Category.objects.get(name=category)
        communities = Community.objects.filter(category=category.id, status='Active')
        category = category.name
    context = {
        'category': category,
        'communities': communities,
    }
    return render(request, 'web/communities.html', context)
