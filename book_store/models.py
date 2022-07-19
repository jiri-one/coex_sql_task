from django.db import models


class Cover(models.Model):
    COVER_TYPE = (("SOFT", "SOFTBACK"), ("HARD", "HARDBACK"), 
    ("SOFT SIGNED", "SOFTBACK SIGNED"), ("HARD SIGNED", "HARDBACK SIGNED"))
    cover = models.CharField(choices=COVER_TYPE, default="SOFT", max_length=200)
    signed_by_author = models.BooleanField(default=False)

    def __str__(self):
        return self.cover

class Book(models.Model):
    name = models.CharField("Book name", max_length=200)
    page_number = models.IntegerField()
    # one-to-many relationship (one book can have only one type of cover, but this same cover can have lot of books)
    cover = models.ForeignKey(Cover, on_delete=models.CASCADE)
    pub_date = models.DateField("Release date")
    genre = models.ManyToManyField("Genre")

    def __str__(self):
        return self.name


class Author(models.Model):
    author = models.CharField("Authors name", max_length=200)
    birth_date = models.DateField('Date of birth')
    book = models.ManyToManyField(Book, through='BookAuthor')

    def __str__(self):
        return self.author


class BookAuthor(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    authors_first_book = models.BooleanField("This is authors first book.", default=False)
    authors_award_for_book = models.BooleanField("The author has received an award for this book.", default=False)

    def __str__(self):
        return f"{self.author.author} - {self.book.name}"


class Genre(models.Model):
    GENRES = (("SCI-FI", "SCI-FI"), ("ACTION", "ACTION"),
               ("FANTASY", "FANTASY"), ("THILER", "THILER"), ("OTHER", "OTHER"))
    genre = models.CharField("Genre of book:", choices=GENRES, default="OTHER", max_length=20)

    def __str__(self):
        return self.genre


# Orders
# Users
# Basket
# Warehouse
# ...
