""" Report Form """

# Django
from django import forms

# Models
from reports.models import ReportModel

class UserReportForm(forms.ModelForm):
    """ User Reports model form """

    class Meta:
        """ Form settings """
        model = ReportModel
        fields = ('communiy_name',
                  'subject',
                  'description',
                  )