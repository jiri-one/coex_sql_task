from django.db import models


class Cover(models.Model):
    COVER_TYPE = (("SOFT", "SOFTBACK"), ("HARD", "HARDBACK"))
    cover = models.CharField(
        choices=COVER_TYPE, default="SOFT", max_length=200)

    def __str__(self):
        return self.cover

class Book(models.Model):
    name = models.CharField("Book name", max_length=200)
    page_number = models.IntegerField()
    # one-to-many relationship (one book can have only one type of cover, but this same cover can have lot of books)
    cover = models.ForeignKey(Cover, on_delete=models.CASCADE)
    pub_date = models.DateField("Release date")

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
    YES_OR_NO = (("Y", "Yes"), ("N", "No"))
    authors_first_book = models.CharField("Is this book authors first book:", 
                                          choices=YES_OR_NO, default="N", max_length=3)
    authors_award_for_book = models.CharField(
        "Recieved author prize for this book:", choices=YES_OR_NO, default="N", max_length=3)

    def __str__(self):
        return f"{self.author.author} - {self.book.name}"


class Gendre(models.Model):
    GENDRES = (("SCI-FI", "SCI-FI"), ("ACTION", "ACTION"),
               ("FANTASY", "FANTASY"), ("THILER", "THILER"), ("OTHER", "OTHER"))
    gender = models.CharField("Gender of book:",
                               choices=GENDRES, default="OTHER", max_length=20)
    book = models.ManyToManyField(Book)

    def __str__(self):
        return self.gender


# Orders
# Users
# Basket
# Warehouse
# ...
