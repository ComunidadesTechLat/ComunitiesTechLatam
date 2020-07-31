""" Communities admin config """
# Django
from django.contrib import admin

# Models
from communities.models import Community

# Register your models here.
admin.site.register(Community)
