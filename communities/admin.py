""" Communities admin config """
# Django
from django.contrib import admin

# Models
from communities.models import Community, Category, Flag


@admin.register(Community)
class CommunityAdmin(admin.ModelAdmin):
    """ Community Admin """

    list_display = ('status', 'name', 'category', 'web', 'facebook_page', 'github', 'country')
    list_display_links = ('name',)
    list_editable = ('status', 'category')

    search_fields = (
        'status',
        'name',
        'country',
    )

    list_filter = ('status', 'created', 'modified')


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass


@admin.register(Flag)
class FlagAdmin(admin.ModelAdmin):
    list_display = ('name', 'icon')
    list_display_links = ('name',)
    list_editable = ('icon',)

    search_fields =(
        'name',
    )