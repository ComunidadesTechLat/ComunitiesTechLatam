''' Communities Tech Latam urls '''

# Django
from django.contrib import admin
from django.urls import path

# Viewa
from web import views as get_views
from communities.views import AddNewCommunity
from reports.views import UserReport


urlpatterns = [

    # web
    path('', get_views.home, name='home'),
    path('about/', get_views.about, name='about'),
    path('events/', get_views.events, name='events'),
    path('contact/', get_views.contact, name='contact'),
    path('community/<uuid:id>', get_views.community, name='community'),
    path('admin/', admin.site.urls),

    # Communities
    path('community/new/', AddNewCommunity.as_view(template_name='community/new.html'), name='new'),

    # User Report
    path('report/', UserReport.as_view(template_name='report.html'), name='report')
]
