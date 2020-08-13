from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Ebook

# Create your views here.


def eBook(request):
    if not request.user.is_authenticated:
        return redirect('accounts:login')

    sql = Ebook.objects.all()
    return render(request, "eBook/ebook.html",{'sql': sql})

