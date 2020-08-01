""" Reports View """

#Django
from django.views.generic import FormView
from django.urls import reverse_lazy

# Froms
from reports.forms import UserReportForm


class UserReport(FormView):
    """ Report a community """

    template_name = 'report.html'
    form_class = UserReportForm
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        """ Save a new report """
        form.save()
        return super().form_valid(form)
