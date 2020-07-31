""" Community Forms """

# Django
from django import forms

# Models
from communities.models import Community

class ComunityForm(forms.ModelForm):
    """ Community model form """

    class Meta: # pylint: disable=too-few-public-methods
        """ Form settings """
        model = Community
        fields = ('name',
                  'logo',
                  'img',
                  'description',
                  'quantity_of_members',
                  'web',
                  'email',
                  'fb_page',
                  'twitter',
                  'instagram',
                  'github',
                  'country',
                  'city',
                  'category',
                  )
