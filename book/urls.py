from django.urls import path
from . import views

urlpatterns = [
    path("books/", views.book_all, name="book_list"),
    path("books/<int:id>/", views.book_detail, name=' books_detail')
]
