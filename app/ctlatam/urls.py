''' Communities Tech Latam urls '''

# Django
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

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
    path('admin/', admin.site.urls),

    # Communities
    path('communities/<str:category>/', get_views.filtered_communities, name='filtered_categories'),
    path('community/new/', AddNewCommunity.as_view(template_name='community/new.html'), name='new'),
    path('community/<uuid:id>', get_views.community, name='community'),
    # User Report
    path('report/', UserReport.as_view(template_name='reports/report.html'), name='report')

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
