from django.contrib import admin
from .models import Movie, Category

class MovieAdmin(admin.ModelAdmin):
    list_display = ('title', 'cat',)

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
admin.site.register(Movie, MovieAdmin)
admin.site.register(Category, CategoryAdmin)
