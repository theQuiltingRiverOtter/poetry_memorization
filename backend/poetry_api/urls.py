from django.urls import path

# Explicit imports
from .views import Poems_By_Author, Poems_By_Title


urlpatterns = [
    path("author/<str:author>", Poems_By_Author.as_view(), name="poems_by_author"),
    path("title/<str:title>", Poems_By_Title.as_view(), name="poems_by_title"),
]
