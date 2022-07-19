# Generated by Django 4.0.6 on 2022-07-19 07:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book_store', '0008_alter_cover_cover_alter_cover_signed_by_author'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookauthor',
            name='authors_award_for_book',
            field=models.BooleanField(default=False, verbose_name='Recieved author prize for this book:'),
        ),
        migrations.AlterField(
            model_name='bookauthor',
            name='authors_first_book',
            field=models.BooleanField(default=False, verbose_name='Is this book authors first book:'),
        ),
    ]
