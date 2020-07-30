"""ctlatam URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from  web import views as get_views
urlpatterns = [
    path('', get_views.home, name='home'),
    path('about/', get_views.about, name='about'),
    path('events/', get_views.events, name='events'),
    path('contact/', get_views.contact, name='contact'),
    path('community/<uuid:id>', get_views.community, name='community'),
    path('admin/', admin.site.urls),
]
