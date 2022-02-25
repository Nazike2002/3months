from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from . import views


app_name = "content"
urlpatterns = [
    path("booksparser/", views.NovelView.as_view(), name="novel"),
    path("anime/", views.AnimeView.as_view(), name="anime"),
    path("parser/", views.ParserAnimeView.as_view(), name="parser"),
]