# coding: utf-8
from django.contrib import admin

from .models import Text, Category



def change_to_upper(modeladmin, request, queryset):
    for i in queryset.all():
        i.name = i.name.upper()
        i.save()
change_to_upper.short_description = u'Nome como maiúsculas'

class TextAdmin(admin.ModelAdmin):
    list_display = ['name', 'filetype', 'modified', 'created', 'is_fresh']
    list_filter = ['filetype', 'created']
    actions = [change_to_upper]


class TextInline(admin.TabularInline):
    model = Text


class CategoryAdmin(admin.ModelAdmin):
    inlines = [TextInline]


admin.site.register(Text, TextAdmin)
admin.site.register(Category, CategoryAdmin)

