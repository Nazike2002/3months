from django.urls import path
from . import views

urlpatterns = [
    path("books/", views.BooksListView.as_view(), name="book_list"),
    path("books/<int:pk>/", views.BooksDetailViews.as_view(), name='books_detail'),
    path("", views.BooksCreateView.as_view(), name="add_books"),
    path("books/<int:id>/delete/", views.BooksDeleteView.as_view(), name="book_delete"),
    path("books/<int:id>/update/", views.BooksUpDateView.as_view(), name="book_update")
]
