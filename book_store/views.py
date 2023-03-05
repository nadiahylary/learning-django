from django.http import Http404
from django.shortcuts import render, get_object_or_404
from .models import Book


# Create your views here.


def index(request):
    book_list = Book.objects.all()
    return render(request, "book_store/index.html", {
        "books": book_list
    })


def detail_book(request, id):
    """try:
        book = Book.objects.get(id=id)
    except:
        raise Http404()"""
    book = get_object_or_404(Book, id=id)
    return render(request, "book_store/detail-book.html", {
        "book": book
    })


def get_book_by_slug(request, slug):
    book = get_object_or_404(Book, slug=slug)
    return render(request, "book_store/detail-book.html", {
        "book": book
    })
