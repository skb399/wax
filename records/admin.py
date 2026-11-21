from django.contrib import admin
from .models import Genre, Record

# Register your models here.

# Admin configuration for the Genre model.
@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    # this shows the fields that will appear as as columns in django admin
    list_display = ('name', 'friendly_name')
    
    # this adds a search box in django admin for easier searching of records by name or friendly name
    search_fields = ('name', 'friendly_name')

# Admin configuration for the Record model.
@admin.register(Record)
class RecordAdmin(admin.ModelAdmin):
     # this shows the fields that will appear as columns django admin
    list_display = (
        'sku',
        'title',
        'artist',
        'genre',
        'price',
        'stock',
        'is_active',
    )
    
    # this adds filters to the right sidebar in django admin for easier filtering of records
    list_filter = ('genre', 'is_active')
    
    # this adds a search box in django admin for easier searching of records by sku, title, or artist
    search_fields = ('sku', 'title', 'artist')
    
    # this automatically populates the slug field based on the title field
    prepopulated_fields = {'slug': ('title',)}