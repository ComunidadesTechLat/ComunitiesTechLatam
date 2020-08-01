""" User Reports admin cofig """

# Django
from django.contrib import admin

# Models
from reports.models import ReportModel

@admin.register(ReportModel)
class ReportAdmin(admin.ModelAdmin):
    """ Reports Admin """

    list_display = ('report_status', 'community_name', 'subject', 'description')
    list_display_links = ('community_name',)
    list_editable = ('report_status',)

    search_fields = (
        'report_status',
        'community_name'
    )

    list_filter = ('report_status', 'created', 'modified')
