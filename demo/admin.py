from demo.models import Book
from django.contrib import admin
from .models import Author, Book, BookNumber, Character
# Register your models here.
#admin.site.register(Book)

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ["title",'price']
    list_filter= ["published"]
    search_fields = ["title",'description']

admin.site.register(BookNumber)
admin.site.register(Character)
admin.site.register(Author)