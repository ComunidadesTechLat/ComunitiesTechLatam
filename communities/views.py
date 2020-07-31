''' Community views '''
#Django
from django.views.generic import FormView
from django.urls import reverse_lazy

# Froms
from communities.forms import Community

# Create your views here.
class AddNewCommunity(FormView): # pylint: disable=too-many-ancestors
    """ Add a new community """

    template_name = 'community/new.html'
    form_class = Community
    success_url = reverse_lazy('/')
