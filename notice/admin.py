from django.contrib import admin
from django.contrib.admin import ModelAdmin

from notice.models import Notice, Type, Category, Condition


# Register your models here.
class NoticeAdmin(ModelAdmin):
    ordering = ['id']
    list_display = ['id', 'name', 'pub_date', 'is_active', 'type', 'category', 'condition', 'user']
    list_display_links = ['id', 'name']
    list_per_page = 20
    list_filter = ['is_active', 'type', 'category', 'condition', 'user']
    search_fields = ['name']


class TypeAdmin(ModelAdmin):
    ordering = ['id']
    list_display = ['id', 'name']


class CategoryAdmin(ModelAdmin):
    ordering = ['id']
    list_display = ['id', 'name']


class ConditionAdmin(ModelAdmin):
    ordering = ['id']
    list_display = ['id', 'name']


admin.site.register(Notice, NoticeAdmin)
admin.site.register(Type, TypeAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Condition, ConditionAdmin)

