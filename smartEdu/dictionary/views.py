from django.shortcuts import render, redirect
from .models import Dictionary
from .models import myDictionary
from django.core.paginator import Paginator
from django.http import HttpResponse, JsonResponse


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


class HttpResponseNoContent(HttpResponse):
    """Special HTTP response with no content, just headers.

    The content operations are ignored.
    """

    def __init__(self, content="", mimetype=None, status=None, content_type=None):
        super().__init__(status=204)

        if "content-type" in self._headers:
            del self._headers["content-type"]

    def _set_content(self, value):
        pass

    def _get_content(self, value):
        pass

def add(request, user, dNO):

    if not request.user.is_authenticated:
        return redirect('accounts:login')

    qs=myDictionary.objects.get(username=user)
    str=qs.arr
    str += "/" + dNO
    qs.arr = str
    qs.save()

    str=str[1:]
    original_list = str.split('/')
   # original_list = list(map(int, original_list))
    erase_duple_list = list(set(original_list))
    erase_duple_list.sort()

    if dNO in erase_duple_list :
        print('이미추가한단어') # 나중에 마저 작성,,

#    qs.list = erase_duple_list
#    qs.save()

    str = ""
    for s in erase_duple_list :
        str += "/" + s

    qs.arr = str
    qs.save()


    #return redirect('dictionary:showDictionary')
    return HttpResponseNoContent()



# ajax 처리. kby_tech
def erase(request, user, dNO):
    # var strurl = "/board_deleteajax?b_no=" + bno;
    # def board_deleteajax(request):
    #     bno = request.GET['b_no']
    if not request.user.is_authenticated:
        return redirect('accounts:login')

    qs=myDictionary.objects.get(username=user)
    str=qs.arr
    str = str[1:]
    original_list = str.split('/')


    original_list.remove(dNO) # 해당 아이템 삭제 [실패시 : valueError ]
    original_list.sort()
    str = ""
    for s in original_list :
        str += "/" + s

    qs.arr = str
    qs.save()



    q_qs = Dictionary.objects.filter(dNO__in=original_list)
    data ={}

    data['result_msg']=" is delete. "

    return JsonResponse(data,content_type="application/json")


    # 현재 페이지 새로고침 추후  ajax로 구현. -완성 : 작성자:KBY_TECH


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









