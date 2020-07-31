''' Communities Tech Latam urls '''

from django.contrib import admin
from django.urls import path
from  web import views as get_views
from communities import views as communities_views


urlpatterns = [
    path('', get_views.home, name='home'),
    path('about/', get_views.about, name='about'),
    path('events/', get_views.events, name='events'),
    path('contact/', get_views.contact, name='contact'),
    path('community/<uuid:id>', get_views.community, name='community'),
    path('admin/', admin.site.urls),

    # Communities
    path('community/new/', communities_views.AddNewCommunity, name='AddNewCommunity'),
]
