# Generated by Django 4.0.6 on 2022-07-18 12:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book_store', '0006_remove_genre_book_book_genre'),
    ]

    operations = [
        migrations.AddField(
            model_name='cover',
            name='signed_by_author',
            field=models.BooleanField(default=True),
        ),
    ]
