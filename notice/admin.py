from django.contrib import admin
from django.contrib.admin import ModelAdmin

from notice.models import Notice


# Register your models here.
class NoticeAdmin(ModelAdmin):
    ordering = ['id']
    list_display = ['id', 'name', 'pub_date', 'is_active', 'type', 'category', 'condition', 'user']
    list_display_links = ['id', 'name']
    list_per_page = 20
    list_filter = ['is_active', 'type', 'category', 'condition', 'user']
    search_fields = ['name']


admin.site.register(Notice, NoticeAdmin)
