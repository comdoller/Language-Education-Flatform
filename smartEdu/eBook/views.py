from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Ebook

# Create your views here.


def eBook(request):
    if not request.user.is_authenticated:
        return redirect('accounts:login')

    sql = Ebook.objects.all()
    return render(request, "eBook/home.html",{'sql': sql})

def viewpdf(request, NO):
    qs = Ebook.objects.get(eNO=NO)
    context = {'ebook_data': qs }
    return render(request, "eBook/ebook.html", context)

