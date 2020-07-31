""" Communities admin config """
# Django
from django.contrib import admin

# Models
from communities.models import Community, Category, Country, Location, Flag

# Register your models here.
admin.site.register(Community)
admin.site.register(Category)
admin.site.register(Country)
admin.site.register(Location)
admin.site.register(Flag)
