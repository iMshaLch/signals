# Generated by Django 3.0 on 2023-05-31 10:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('page_profile', '0002_book'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='author',
            field=models.ManyToManyField(to='page_profile.Profile'),
        ),
    ]