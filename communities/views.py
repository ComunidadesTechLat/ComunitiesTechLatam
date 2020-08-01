''' Community views '''
#Django
from django.views.generic import FormView
from django.urls import reverse_lazy

# Froms
from communities.forms import ComunityForm

# Create your views here.
class AddNewCommunity(FormView): # pylint: disable=too-many-ancestors
    """ Add a new community """

    template_name = 'community/new.html'
    form_class = ComunityForm
    success_url = reverse_lazy('/')
