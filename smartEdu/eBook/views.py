from django.shortcuts import render
from django.http import HttpResponse
from .models import Ebook

# Create your views here.


def eBook(request):
    sql = Ebook.objects.all()
    return render(request, "ebook/ebook.html",{'sql': sql})

