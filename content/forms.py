from django import forms
from content import models
from content.parser import parser


class ParserForm(forms.Form):
    MEDIA_CHOICES = (
        ("Anime", "Anime"),
        ("Books", "Books")
    )
    media_type = forms.ChoiceField(choices=MEDIA_CHOICES)
    class meta:
        fields = [
            "media_type",
        ]


    def parser_data(self):
        if self.data["media_type"] == "Anime":
            anime_data = parser()
            for i in anime_data:
                models.Anime.objects.create(**i)

        elif self.data["media_type"] == "Books":
            books_data = parser()
            for i in books_data:
                models.Novel.objects.create(**i)