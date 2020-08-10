from django.shortcuts import render, redirect
from django.http import HttpResponse

##def home(request):
##    return HttpResponse("강원대학교 산학협력 프로젝트")


def home(request):
    return render(request, 'home/index.html')