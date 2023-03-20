from django.contrib import admin
from .models import Tag

# Register your models hermodelse.
@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    search_fields = ['label']