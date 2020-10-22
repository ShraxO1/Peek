from django.contrib import admin
from .models import People
# Register your models here.

@admin.register(People)
class PeopleAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug', 'image', 'created']
    list_filter = ['created']
