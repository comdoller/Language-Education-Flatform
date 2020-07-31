from django.shortcuts import render
from dictionary.models import Dictionary
from django.core.paginator import Paginator
from django.http import HttpResponse

# Create your views here.


def showDictionary(request):

    qs = Dictionary.objects.all()
    context = {'dictionaryAll': qs}
    return render(request, "dictionary.html", context)

def search(request):
    qs = Dictionary.objects.all()
    q = request.GET.get('q','')
    if q:
        qs = qs.filter(dTetum=q) or qs.filter(dEnglish=q) or qs.filter(dBahasa=q) or qs.filter(dKorea=q) or qs.filter(dJapan=q)

        return render(request, 'dictionary.html', {
            'search_result' : qs,
            'q': q,
        })