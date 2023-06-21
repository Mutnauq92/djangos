from django.urls import path
from api1.views import hello, book_list

urlpatterns = [
    path("", hello, name="hello"),
    path("book_list/", book_list, name="book_list"),
    path("book_list/<int:pk>/", book_list, name="book_list"),
]
