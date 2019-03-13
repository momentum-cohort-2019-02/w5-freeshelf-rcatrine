from django.db import models

# Create your models here.

class Author(models.Model):
    """Model representing an author."""
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

    class Meta:
        ordering = ['last_name', 'first_name']
    
    def get_absolute_url(self):
        """Returns the url to access a particular author instance."""
        return reverse('author-detail', args=[str(self.id)])

    def __str__(self):
        """String for representing the Model object."""
        return f'{self.last_name}, {self.first_name}'

class Book(models.Model):
    """Model representing a book."""
    title = models.CharField(max_length=200, default='N/A', help_text='Enter the name of a free to access programming book.')
    author = models.CharField(max_length=200, default='N/A', help_text='Enter the name of the author.')
    category_or_Programming_Language = models.CharField(max_length=200, default='N/A', help_text='Enter the category/programming language of the book.')  
    description = models.TextField(max_length=1000, default='N/A', help_text='Enter a description of the book.')
    date_added = models.DateTimeField(auto_now_add=True)
    uRL = models.TextField(max_length=1000, default='N/A', help_text='Enter the URL of the book.')
    slug = models.TextField(max_length=1000, default='N/A', help_text='Enter the URL slug.')
    
    def __str__(self):
        """String for representing the Model object."""
        return self.title
    
class Category(models.Model):
    """Model representing a category."""
    title = models.CharField(max_length=200, default='N/A', help_text='Enter the name of a free to access programming book.')
    author = models.CharField(max_length=200, default='N/A', help_text='Enter the name of the author.')
    category_or_Programming_Language = models.CharField(max_length=200, default='N/A', help_text='Enter the category/programming language of the book.')  
    description = models.TextField(max_length=1000, default='N/A', help_text='Enter a description of the book.')
    date_added = models.DateTimeField(auto_now_add=True)
    uRL = models.TextField(max_length=1000, default='N/A', help_text='Enter the URL of the book.')
    slug = models.TextField(max_length=1000, default='N/A', help_text='Enter the URL slug.')
    
    def __str__(self):
        """String for representing the Model object."""
        return self.title

# class Favorites(models.Model)
    
