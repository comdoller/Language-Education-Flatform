from django.shortcuts import render, redirect
from .models import Dictionary
import random
from django.db.models import Q

global test_list
global testR
global testQS

def dTest_main(request):

    if not request.user.is_authenticated:
        return redirect('accounts:login')

    return render(request, "dTest/dTest_main.html")

def dTest(request):
    global test_list
    global testR
    global testQS
    test_list = []
    ran_num = random.randint(1, 1478)
    testR = request.GET.get('testR')
    exR = request.GET.getlist('exR')
    if not exR:
        return render(request, "dTest/dTest_main.html", {"empty_error" : "보기 언어를 하나 이상 선택해주세요."})
    for R in exR:
        if R==testR:
            return render(request, "dTest/dTest_main.html", {"error" : "시험 볼 언어와 보기 언어는 같은 언어를 선택 할 수 없습니다."})
    for i in range(20):
        while ran_num in test_list:
            ran_num = random.randint(1, 1478)
        test_list.append(ran_num)
    test_list.sort()

    testQS = Dictionary.objects.filter(Q(dNO=test_list[0]) | Q(dNO=test_list[1]) | Q(dNO=test_list[2]) | Q(dNO=test_list[3]) | Q(dNO=test_list[4]) |
                                     Q(dNO=test_list[5]) | Q(dNO=test_list[6]) | Q(dNO=test_list[7]) | Q(dNO=test_list[8]) | Q(dNO=test_list[9]) |
                                     Q(dNO=test_list[10]) | Q(dNO=test_list[11]) | Q(dNO=test_list[12]) | Q(dNO=test_list[13]) | Q(dNO=test_list[14]) |
                                     Q(dNO=test_list[15]) | Q(dNO=test_list[16]) | Q(dNO=test_list[17]) | Q(dNO=test_list[18]) | Q(dNO=test_list[19]) )

    return render(request, "dTest/dTest_exam.html", {"testQS" : testQS ,
                                                     "testR" : testR,
                                                     "exR" : exR})

def result(request):



    answer_list = request.GET.getlist('answer')

    score = 0

    if testR == "테툼어":
        for i, word in enumerate(testQS):
            if word.dTetum == answer_list[i]:
                score+=1

    if testR == "영어":
        for i, word in enumerate(testQS):
            if word.dEnglish == answer_list[i]:
                score+=1

    if testR == "바하사":
        for i, word in enumerate(testQS):
            if word.dBahasa == answer_list[i]:
                score+=1

    if testR == "한국어":
        for i, word in enumerate(testQS):
            if word.dKorea == answer_list[i]:
                score+=1

    if testR == "일어":
        for i, word in enumerate(testQS):
            if word.dJapan == answer_list[i]:
                score+=1


    return render(request, "dTest/dTest_result.html", {"score" : score,
                                                       "answer_list" : answer_list,
                                                       "testR": testR,
                                                       "testQS": testQS})
