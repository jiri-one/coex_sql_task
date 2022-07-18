from django.contrib import admin

from .models import Cover, Book, Author, BookAuthor, Genre

for model in [Cover, Book, Author, BookAuthor, Genre]:
    admin.site.register(model)
