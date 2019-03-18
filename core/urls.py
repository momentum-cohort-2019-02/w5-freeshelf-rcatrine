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

    path('awk/', views.awkListView.as_view(), name='awk'),
    path('awk/<int:pk>', views.awkDetailView.as_view(), name='awk-detail'),

    path('bash/', views.bashListView.as_view(), name='bash'),
    path('bash/<int:pk>', views.bashDetailView.as_view(), name='bash-detail'),

    path('html/', views.htmlListView.as_view(), name='html'),
    path('html/<int:pk>', views.htmlDetailView.as_view(), name='html-detail'),

    path('javascript/', views.javascriptListView.as_view(), name='javascript'),
    path('javascript/<int:pk>', views.javascriptDetailView.as_view(), name='javascript-detail'),

    path('ruby/', views.rubyListView.as_view(), name='ruby'),
    path('ruby/<int:pk>', views.rubyDetailView.as_view(), name='ruby-detail'),
    
    url(r'register/$', views.register, name='register'),
    
]