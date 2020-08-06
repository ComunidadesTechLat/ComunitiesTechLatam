""" Report Form """

# Django
from django import forms

# Models
from reports.models import ReportModel

class UserReportForm(forms.ModelForm):
    """ User Reports model form """

    class Meta: # pylint: disable=too-few-public-methods
        """ Form settings """
        model = ReportModel
        fields = ('community_name',
                  'subject',
                  'description',
                  )
