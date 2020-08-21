from django.shortcuts import render, redirect
from .models import Dictionary
from django.core.paginator import Paginator
from django.http import HttpResponse

# Create your views here.

def showDictionary(request):

    if not request.user.is_authenticated:
        return redirect('accounts:login')

    qs = Dictionary.objects.all()
    page = int(request.GET.get('p', 1))
    paginator = Paginator(qs, 20)
    context = paginator.get_page(page)
    return render(request, "dictionary/dictionary.html", {"dictionaryAll": context})

def search(request):

    if not request.user.is_authenticated:
        return redirect('accounts:login')

    qs = Dictionary.objects.all()
    q = request.GET.get('q','')
    if q:
        qs = qs.filter(dTetum=q) or qs.filter(dEnglish=q) or qs.filter(dBahasa=q) or qs.filter(dKorea=q) or qs.filter(dJapan=q)

        return render(request, 'dictionary/dictionary.html', {
            'search_result' : qs,
            'q': q,
        })