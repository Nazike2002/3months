from django.http import Http404, HttpResponse
from django.shortcuts import reverse, redirect, render, get_object_or_404
from django.views import generic
from . import models, forms


class BooksListView(generic.ListView):
    template_name = "book_list.html"
    queryset = models.Book.objects.all()
    context_object_name = 'book'

    # def get_queryset(self):
    #     return self.queryset


# def book_all(request):
#     book = models.Book.objects.all()
#     return render(request, "book_list.html", {"book": book})

class BooksDetailViews(generic.DetailView):
    template_name = "book_detail.html"
    context_object_name = 'book'
    def get_object(self, **kwargs):
        books_id = self.kwargs.get("pk")
        return get_object_or_404(models.Book, pk=books_id)




class BooksCreateView(generic.CreateView):
    template_name = "add_book_list.html"
    form_class = forms.Book_form
    queryset = models.Book.objects.all()
    success_url = "/books/"

    def form_valid(self, form):
        print(form.cleaned_data)
        return super(BooksCreateView, self).form_valid(form=form)
# def book_update(request, id):
#     book_id = get_object_or_404(models.Book, id=id)
#     if request.method == "POST":
#         form = forms.Book_form(instance=book_id,
#                                data=request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect("/books/")
#     else:
#         form = forms.Book_form(instance=book_id)
#     return render(request, "books_update.html", {"form": form,
#                                                  "book": book_id})
class BooksUpDateView(generic.UpdateView):
    template_name = "books_update.html"
    form_class = forms.Book_form
    success_url ="/books/"

    def get_object(self, **kwargs):
        books_id =  self.kwargs.get("id")
        return get_object_or_404(models.Book, pk=books_id)

    def form_valid(self, form):
        print(form.cleaned_data)
        return super(BooksUpDateView, self).form_valid(form=form)


class BooksDeleteView(generic.DeleteView):
    success_url = "/books/"
    template_name = "confirm_delete_book.html"

    def get_object(self, **kwargs):
        books_id = self.kwargs.get("id")
        return get_object_or_404(models.Book, pk=books_id)

# def book_delete(request, id):
#     book_id = get_object_or_404(models.Book, id=id)
#     book_id.delete()
#     return redirect("/books/")
#
#
# # return HttpResponse("Show Deleted")
#
#
# def book_detail(request, id):
#     global review
#     try:
#         book = get_object_or_404(models.Book, id=id)
#         try:
#             review = models.Review.objects.filter(book_id=id).order_by("created_date")
#         except models.Book.DoesNotExist:
#             print("Not review")
#     except models.Book.DoesNotExist:
#         raise Http404('Book does not exist, try another id')
#     return render(request, "book_detail.html", {"review": review, "book": book})


# def author(request, id):
#     global author
#     try:
#         book = get_object_or_404(models.Book, id=id)
#         try:
#             author = models.Author.objects.filter(name_id=id).order_by("name")
#         except models.Book.DoesNotExist:
#             print("Not author ")
#     except models.Book.DoesNotExist:
#         raise Http404('Author does not exist, try another id')
#     return render(request, "book_detail.html", {'book': book, "author": author})
#

def add_books(request):
    method = request.method
    if method == "POST":
        form = forms.Book_form(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            # return redirect(reverse("books : book_list.html"))
            return redirect("/books/")

    else:
        form = forms.Book_form()
    return render(request, "add_book_list.html", {"form": form})
