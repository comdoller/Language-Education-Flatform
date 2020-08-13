from django.shortcuts import render
from django.http import HttpResponse
from .models import Ebook


# Create your views here.


def down(request):
    sql = Ebook.objects.all()
    return render(request, "down/down.html",{'sql': sql})

#여기서부터 작성#






