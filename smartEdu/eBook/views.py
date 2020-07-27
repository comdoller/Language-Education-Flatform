from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def eBook(request):
    return render(request, 'ebook.html')

