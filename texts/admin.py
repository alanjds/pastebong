from django.contrib import admin

from .models import Text, Category

# Register your models here.

admin.site.register(Text)
admin.site.register(Category)