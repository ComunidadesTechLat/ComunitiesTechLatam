''' Community views '''
#Django
from django.shortcuts import render, redirect
from django.views.generic import FormView
from django.urls import reverse_lazy

# Froms
from communities.forms import Community

# Create your views here.
class AddNewCommunity(FormView):
    """ Add a new community """

    template_name = 'community/new.html'
    form_class = Community
    success_url = reverse_lazy('/')
