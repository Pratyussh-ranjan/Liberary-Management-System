from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Book(models.Model):
    isbn = models.CharField(max_length=13)  # Example field definition
    published_date = models.DateField()

    def __str__(self):
        return self.title
