from django.contrib import admin
from core.models import Author, Book 

# Register your models here.
# admin.site.register(Book)
# admin.site.register(Author)
# admin.site.register(Book)

# Define the admin class
admin.site.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name')
    fields = ['first_name', 'last_name']

# Register the Admin classes for Book using the decorator
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author')