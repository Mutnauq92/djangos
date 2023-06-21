from django.shortcuts import render

# Create your views here.
from django.http import JsonResponse

def hello(request):
    return JsonResponse({"Message": "Hello World !!!"})

def book_list(request, pk=None):
    books = [
        {"title": "Book 1", "author": "Author 1"},
        {"title": "Book 2", "author": "Author 2"},
        {"title": "Book 3", "author": "Author 3"},
        {"title": "Book 4", "author": "Author 4"},
        {"title": "Book 5", "author": "Author 5"},
    ]
    if not pk is None:
        for index, book in enumerate(books):
            if pk <= len(books):
                if pk == index + 1:
                    return JsonResponse({"title": books[index]["title"]})
        return JsonResponse({"error": "Book not found !"}, status=404)    
    return JsonResponse({"books": books})


















