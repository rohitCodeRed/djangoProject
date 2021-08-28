from typing import ValuesView
from django.http.response import HttpResponse
from django.shortcuts import render
from django.views import View
from .models import Book

# Create your views here.
class Another(View):
    books = Book.objects.all() #.filter
    output=''
    for book in books:
        output += f"{book.title} <br>"

    def get(self, request):
        return HttpResponse(self.output)




def first(request):
    return render(request,'first_temp.html',{"books":{"title":"hi there"}})