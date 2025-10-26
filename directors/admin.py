from django.contrib import admin
from directors.models import Directors


@admin.register(Directors)
class DirectorAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'birthday', 'nationality',)
    search_fields = ('id', 'name', 'nationality',)
