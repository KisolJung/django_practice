from django.shortcuts import render, redirect, get_object_or_404
from .forms import CreateBoard, CreateComment, UploadFileForm
from .models import Board, Comment, UploadFile
from django.core.files.storage import FileSystemStorage
from django.db import connection
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator


# INDEX
def index(request):
    return render(request, 'index.html')


# 게시판 메이페이지
def boardMain(request):
    page = request.GET.get('page', '1')
    board_list = Board.objects.order_by('-id')
    print(board_list.query)
    paginator = Paginator(board_list, 10)
    boards = paginator.get_page(page)
    context = {
        'boards': boards
    }

    return render(request, 'boardMain.html', context)


# boad와 파일 여러개 업로드
@login_required(login_url='common:login')
def create_board_multiFile(request):
    if request.method == "POST":
        board_form = CreateBoard(request.POST)
        file_form = UploadFileForm(request.POST, request.FILES)
        if board_form.is_valid():
            new_board = board_form.save(commit=False)
            new_board.author = request.user
            new_board.save()
            printQuery()
            board_id = Board.objects.latest('id').id
            if file_form.is_valid():
                files = request.FILES.getlist('file')
                upload_file_list = []
                for f in files:
                    # new_files = file_form.save(commit=False)
                    upload_file_list.append(UploadFile(file=f, board_id=board_id, org_file_name=f.name))
                UploadFile.objects.bulk_create(upload_file_list)
                printQuery()
                return redirect('boardApp:boardMain')
    else:
        context = {
            'board_form': CreateBoard(),
            'file_form': UploadFileForm()
        }
        return render(request, 'multiUpload.html', context)


# board 자세히 보기
def detail(request, board_id):
    board_detail = get_object_or_404(Board, pk=board_id)
    comments = Comment.objects.filter(board_id=board_id).order_by('-id')
    upload_file = UploadFile.objects.filter(board_id=board_id).order_by('-id')
    print(comments.query)
    print(upload_file.query)

    comment_form = CreateComment()

    context = {
        'board_detail': board_detail,
        'upload_file': upload_file,
        'comments': comments,
        'comment_form': comment_form
    }

    if request.method == "POST":
        comment_form = CreateComment(request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.board_id = board_id
            user = request.user
            if user.is_authenticated:
                new_comment.author = request.user
                new_comment.save()
                printQuery()

    return render(request, 'detail.html', context)


# Select 외의 dml 출력
def printQuery():
    line = "=-=-=-=--=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-"
    print(line + line)
    print(connection.queries[-1])
    print(line + line)
