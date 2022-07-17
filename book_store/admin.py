from django.contrib import admin

from .models import Cover, Book, Author, BookAuthor, Gendre

for model in [Cover, Book, Author, BookAuthor, Gendre]:
    admin.site.register(model)
