""" Community Forms """

# Django
from django import forms

# Models
from communities.models import Community

class ComunityForm(forms.ModelForm):
    """ Community model form """

    class Meta:
        """ Form settings """
        model = Community
        fields = ('name',
                  'logo',
                  'description',
                  'q_members',
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
