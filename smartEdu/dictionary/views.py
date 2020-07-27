from django.shortcuts import render
from dictionary.models import Dictionary
from django.core.paginator import Paginator
from django.http import HttpResponse

# Create your views here.


def showDictionary(request):

    qs = Dictionary.objects.all()
    context = {'dictionaryAll': qs}
    return render(request, "dictionary.html", context)