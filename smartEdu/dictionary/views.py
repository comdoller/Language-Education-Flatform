from django.shortcuts import render, redirect
from .models import Dictionary
from .models import myDictionary
from django.core.paginator import Paginator
from django.contrib import auth

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

def add(request, user, dNO):

    if not request.user.is_authenticated:
        return redirect('accounts:login')

    qs=myDictionary.objects.get(username=user)
    str=qs.arr
    str += "/" + dNO
    qs.arr = str
    qs.save()

    return redirect('dictionary:showDictionary')

def mydictionary(request, user):

    if not request.user.is_authenticated:
        return redirect('accounts:login')

    if request.user.username != user:
        return render(request, 'dictionary/dictionary.html', {'account_error': '본인의 단어장만 열람할 수 있습니다.'})

    qs = myDictionary.objects.get(username=user)

    if qs.arr:
        str = qs.arr
        q_str=str[1:]
        list = q_str.split('/')
        list.sort
        q_qs = Dictionary.objects.filter(dNO__in=list)
        return render(request, 'dictionary/mydictionary.html', {"list":q_qs} )

    return render(request, 'dictionary/mydictionary.html')









