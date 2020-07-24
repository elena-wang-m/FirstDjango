from django.shortcuts import render
from django.http import  HttpResponse
from .models import Book

# Create your views here.
def index(request):
    return HttpResponse("Labrary Management System")

def detail(request, id):
    book = Book.objects.get(id=id)
    info = """
    book id: %s
    book name: %s
    book up_date: %s
    """ %(book.id, book.title, book.pub_date)
    return HttpResponse(info)