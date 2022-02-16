from django.shortcuts import render
from . import models, forms
from django.shortcuts import get_object_or_404
from django.shortcuts import reverse, redirect
from django.http import Http404, HttpResponse

def book_all(request):
    book = models.Book.objects.all()
    return render(request, "book_list.html", {"book": book})


def book_detail(request, id):
    global review
    try:
        book = get_object_or_404(models.Book, id=id)
        try:
            review = models.Review.objects.filter(book_id=id).order_by("created_date")
        except models.Book.DoesNotExist:
            print("Not review")
    except models.Book.DoesNotExist:
        raise Http404('Book does not exist, try another id')
    return render(request, "book_detail.html", {"review": review, "book": book})


def author(request, id):
    global author
    try:
        book = get_object_or_404(models.Book, id=id)
        try:
            author = models.Author.objects.filter(name_id=id).order_by("name")
        except models.Book.DoesNotExist:
            print("Not author ")
    except models.Book.DoesNotExist:
        raise Http404('Author does not exist, try another id')
    return render(request, "book_detail.html", {'book': book, "review": review, "author": author})


def add_books(request):
    method = request.method
    if method =="POST":
        form = forms.Book_form(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            # return redirect(reverse("books : book_list.html"))
            return HttpResponse("Books Created Successfully")

    else:
        form = forms.Book_form()
    return render(request, "add_book_list.html", {"form": form})

