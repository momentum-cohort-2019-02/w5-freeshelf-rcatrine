from django.contrib import admin
from core.models import Author, Book, Category 

# Register your models here.
# admin.site.register(Book)
# admin.site.register(Author)
# admin.site.register(Book)

# Define the admin class
admin.site.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name')
    fields = ['first_name', 'last_name']

# Register the Admin classes for Book and Category using the decorator
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author')

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'author')