from django.http import Http404
from django.shortcuts import render, get_object_or_404
from . import models


def book_all(request):
    book = models.Book.objects.all()
    return render(request, "book_list.html", {"book": book})


def book_detail(request, id):
    try:
        book = get_object_or_404(models.Book, id=id)
        try:
            review = models.Review.objects.filter(book_id=id).order_by("created_date")
        except models.Book.DoesNotExist:
            print("Not review")
    except models.Book.DoesNotExist:
        raise Http404('Book does not exist, try another id')
    return render(request, "book_detail.html", {'book': book, "review": review})
