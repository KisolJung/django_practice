from django.shortcuts import render, redirect, get_object_or_404
from .forms import CreateBoard, CreateComment
from .models import Board, Comment
from django.core.files.storage import FileSystemStorage
from django.db import connection
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    return render(request, 'index.html')

def boardMain(request):
    boards = Board.objects.all().order_by('-id')
    print(boards.query)
    return render(request, 'boardMain.html', {'boards': boards})


@login_required(login_url='common:login')
def createBoard_File(request):
    if request.method == 'POST':
        form = CreateBoard(request.POST, request.FILES)
        if form.is_valid():
            #print(form)
            new_board = form.save(commit=False)
            user = request.user
            if user.is_authenticated:
                new_board.author = request.user
            else:
                redirect('boardApp:boardMain')
            if request.FILES.get('file_path'):
                file_name = request.FILES.get('file_path').name
                new_board.file_name = file_name
            new_board.save()
            printQuery()

            return redirect('boardApp:boardMain')
        else:
            return redirect('boardApp:index')
    else:
        form = CreateBoard()
        return render(request, 'createBoard_file.html', {'form': form})


def detail(request, board_id):
    board_detail = get_object_or_404(Board, pk=board_id)
    comments = Comment.objects.filter(board_id=board_id).order_by('-id')
    print(comments.query)

    comment_form = CreateComment()

    context = {
        'board_detail': board_detail,
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


def uploadFile(request):
    if request.method == 'POST' and request.FILES['myFile']:
        myfile = request.FILES['myFile']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        uploaded_file_url = fs.url(filename)
        return render(request, 'uploadSample.html', {'uploaded_file_url': uploaded_file_url})
    return render(request, 'uploadSample.html')


def printQuery():
    line = "=-=-=-=--=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-"
    print(line+line)
    print(connection.queries[-1])
    print(line+line)