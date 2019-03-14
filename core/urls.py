from django.urls import path
from . import views
from django.db import models
from django.urls import reverse

from django.conf.urls import url




urlpatterns = [
    path('', views.index, name='index'),
    path('books/', views.BookListView.as_view(), name='books'),
    path('book/<int:pk>', views.BookDetailView.as_view(), name='book-detail'),
    path('categories/', views.CategoryListView.as_view(), name='categories'),
    path('categories/<int:pk>', views.CategoryDetailView.as_view(), name='category-detail'),
    url(r'register/$', views.register, name='register'),
    
]