from django import forms
from .models import Book, Author

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['isbn', 'published_date', ...]  # Include other fields as needed

class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = ['name', 'email', ...]  # Include other fields as needed
