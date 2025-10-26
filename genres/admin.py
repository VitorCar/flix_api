from django.contrib import admin
from genres.models import Genre
# Register your models here.


@admin.register(Genre)
class GerenAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('name',)
