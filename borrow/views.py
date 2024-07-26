from django.shortcuts import render, redirect, get_object_or_404
from library.models import Book
from .models import Borrow
from django.contrib.auth.decorators import login_required
from django.utils import timezone

@login_required
def borrow_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    if book.available_copies > 0:
        Borrow.objects.create(user=request.user, book=book)
        book.available_copies -= 1
        book.save()
    return redirect('book_list')

@login_required
def return_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    borrow = get_object_or_404(Borrow, book=book, user=request.user, returned_at__isnull=True)
    borrow.returned_at = timezone.now()
    borrow.save()
    book.available_copies += 1
    book.save()
    return redirect('book_list')

@login_required
def borrow_list(request):
    borrows = Borrow.objects.filter(user=request.user, returned_at__isnull=True)
    return render(request, 'borrow/borrow_list.html', {'borrows': borrows})
