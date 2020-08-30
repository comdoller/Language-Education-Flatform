import os

from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.utils.http import urlquote
from django.views.decorators.csrf import csrf_exempt
from django.contrib import auth

from .models import Board,Comment

# Create your views here.
def board(request):

    if not request.user.is_authenticated:
        return redirect('accounts:login')

    boardCount = Board.objects.count()
    boardList = Board.objects.all().order_by("-idx")
    return render(request, "board.html", {"boardList" : boardList, "boardCount" : boardCount})


def write(request):

    if not request.user.is_authenticated:
        return redirect('accounts:login')

    return render(request,"write.html")

##여기##
UPLOAD_DIR = os.getcwd()

#
@csrf_exempt
def insert(request):

    if not request.user.is_authenticated:
        return redirect('accounts:login')

    fname = ""
    fsize = 0
    if "file" in request.FILES:
        file = request.FILES["file"]
        fname = file.name
        fsize = file.size
        fp = open("%s%s" % (UPLOAD_DIR, fname), "wb")
        for chunk in file.chunks():
            fp.write(chunk)
        fp.close()

    dto = Board(writer=request.user.username, title=request.POST.get("title",''), content=request.POST.get("content",''),
                filename=fname, filesize=fsize)
    dto.save()
    print(dto)
    return redirect("/board")

#다운로드
def download(request):
    id = request.GET['idx']
    dto = Board.objects.get(idx = id)
    path = UPLOAD_DIR + dto.filename
    filename = os.path.basename(path)
    filename = filename.encode('utf-8')
    filename = urlquote(filename)
    with open(path, 'rb') as file:
        response = HttpResponse(file.read(), content_type = "application/octet-stream")
        response["Content-Disposition"] = "attachment; filename* = UTF-8''{0}".format(filename)
        dto.down_up()
        dto.save()
        return response

#상세보기페이지
def detail(request):

    if not request.user.is_authenticated:
        return redirect('accounts:login')

    id = request.GET["idx"]
    dto = Board.objects.get(idx=id)
    dto.hit_up()
    dto.save()

    commentList = Comment.objects.filter(board_idx = id).order_by("idx")

    print("filesize : ", dto.filesize)
    filesize = "%.2f" % (dto.filesize / 1024)
    return render(request, "detail.html", {"dto": dto, "filesize": filesize, "commentList":commentList})

#수정페이지
@csrf_exempt
def modify(request):

    if not request.user.is_authenticated:
        return redirect('accounts:login')

    id = request.GET["idx"]
    dto = Board.objects.get(idx=id)

    filesize = "%.2f" % (dto.filesize / 1024)
    return render(request, "modify.html", {"dto": dto, "filesize": filesize})


#수정
@csrf_exempt
def update(request):

    if not request.user.is_authenticated:
        return redirect('accounts:login')

    id = request.POST['idx']
    dto_src = Board.objects.get(idx=id)
    fname = dto_src.filename
    fsize = 0
    if "file" in request.FILES:
        file = request.FILES["file"]
        fname = file.name
        # fsize = file.size
        fp = open("%s%s" % (UPLOAD_DIR, fname), "wb")
        for chunk in file.chunks():
            fp.write(chunk)
        fp.close()

        fsize = os.path.getsize(UPLOAD_DIR + fname)

    dto_new = Board(idx=id, writer=request.POST["writer"], title=request.POST.get("title",''), content=request.POST.get("content",''),
                    filename=fname, filesize=fsize)
    dto_new.save()
    return redirect("/board")


@csrf_exempt
def delete(request):

    if not request.user.is_authenticated:
        return redirect('accounts:login')

    id = request.POST['idx']
    Board.objects.get(idx = id).delete()
    return redirect("/board")


@csrf_exempt
def reply_insert(request):

    if not request.user.is_authenticated:
        return redirect('accounts:login')

    id = request.POST['idx']
    dto = Comment(board_idx=id, writer=request.POST.get("writer",''), content=request.POST.get("content",''))
    dto.save()
    return HttpResponseRedirect("detail?idx="+id)


##################내 list 부분 ########################
def list(request):

    if not request.user.is_authenticated:
        return redirect('accounts:login')

    boardCount = Board.objects.count()
    boardList = Board.objects.all().order_by("-idx")
    return render(request, "list.html", {"boardList" : boardList, "boardCount" : boardCount})

#나의 수정
@csrf_exempt
def my_update(request):

    if not request.user.is_authenticated:
        return redirect('accounts:login')

    id = request.POST['idx']
    dto_src = Board.objects.get(idx=id)
    fname = dto_src.filename
    fsize = 0
    if "file" in request.FILES:
        file = request.FILES["file"]
        fname = file.name
        # fsize = file.size
        fp = open("%s%s" % (UPLOAD_DIR, fname), "wb")
        for chunk in file.chunks():
            fp.write(chunk)
        fp.close()

        fsize = os.path.getsize(UPLOAD_DIR + fname)

    dto_new = Board(idx=id, writer=request.POST["writer"], title=request.POST.get("title",''), content=request.POST.get("content",''),
                    filename=fname, filesize=fsize)
    dto_new.save()

    boardCount = Board.objects.count()
    boardList = Board.objects.all().order_by("-idx")
    return render(request, "list.html", {"boardList": boardList, "boardCount": boardCount})

#나의_수정페이지
@csrf_exempt
def my_modify(request):

    if not request.user.is_authenticated:
        return redirect('accounts:login')

    id = request.GET["idx"]
    dto = Board.objects.get(idx=id)

    filesize = "%.2f" % (dto.filesize / 1024)
    return render(request, "my_modify.html", {"dto": dto, "filesize": filesize})

#나의_상세보기페이지
def my_detail(request):

    if not request.user.is_authenticated:
        return redirect('accounts:login')

    id = request.GET["idx"]
    dto = Board.objects.get(idx=id)
    dto.hit_up()
    dto.save()

    commentList = Comment.objects.filter(board_idx = id).order_by("idx")

    print("filesize : ", dto.filesize)
    filesize = "%.2f" % (dto.filesize / 1024)
    return render(request, "my_detail.html", {"dto": dto, "filesize": filesize, "commentList":commentList})

@csrf_exempt
def my_delete(request):

    if not request.user.is_authenticated:
        return redirect('accounts:login')

    id = request.POST['idx']
    Board.objects.get(idx = id).delete()

    boardCount = Board.objects.count()
    boardList = Board.objects.all().order_by("-idx")
    return render(request, "list.html", {"boardList": boardList, "boardCount": boardCount})

@csrf_exempt
def my_reply_insert(request):

    if not request.user.is_authenticated:
        return redirect('accounts:login')

    id = request.POST['idx']
    dto = Comment(board_idx=id, writer=request.POST.get("writer",''), content=request.POST.get("content",''))
    dto.save()
    return HttpResponseRedirect("my_detail?idx="+id)


















