from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("<int:id>", views.detail_book, name="book-detail"),
    path("<slug:slug>", views.get_book_by_slug, name="book-detail-slug")
]
