# Generated by Django 2.1.7 on 2019-03-11 21:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_auto_20190311_1734'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='programming_Language',
        ),
        migrations.AddField(
            model_name='book',
            name='category_or_Programming_Language',
            field=models.CharField(default='N/A', help_text='Enter the category/programming language of the book.', max_length=200),
        ),
    ]
