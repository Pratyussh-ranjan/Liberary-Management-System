from django.test import TestCase
from .models import Book, Author

class AuthorModelTest(TestCase):
    def setUp(self):
        Author.objects.create(name="Author Name")

    def test_author_creation(self):
        author = Author.objects.get(name="Author Name")
        self.assertTrue(isinstance(author, Author))
        self.assertEqual(author.__str__(), author.name)

class BookModelTest(TestCase):
    def setUp(self):
        author = Author.objects.create(name="Author Name")
        Book.objects.create(title="Book Title", author=author)

    def test_book_creation(self):
        book = Book.objects.get(title="Book Title")
        self.assertTrue(isinstance(book, Book))
        self.assertEqual(book.__str__(), book.title)
