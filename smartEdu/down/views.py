from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Ebook

# Create your views here.


def down(request):

    if not request.user.is_authenticated:
        return redirect('accounts:login')

    sql = Ebook.objects.all()
    return render(request, "down/down.html",{'sql': sql})

