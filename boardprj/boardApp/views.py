from django.shortcuts import render, redirect, get_object_or_404
from .forms import CreateBoard
from .models import Board
from django.core.files.storage import FileSystemStorage
from django.db import connection

# Create your views here.
def index(request):
    return render(request, 'index.html')

def boardMain(request):
    boards = Board.objects.all().order_by('-id')
    print(boards.query)
    return render(request, 'boardMain.html', {'boards': boards})



def createBoard_File(request):
    if request.method == 'POST':
        form = CreateBoard(request.POST, request.FILES)
        if form.is_valid():
            #print(form)
            if request.FILES.get('file_path'):
                file_name = request.FILES.get('file_path').name
                new_board = form.save(commit=False)
                new_board.file_name = file_name
                new_board.save()
                printQuery()
            else:
                form.save()
                printQuery()

            return redirect('boardApp:boardMain')
        else:
            return redirect('boardApp:index')
    else:
        form = CreateBoard()
        return render(request, 'createBoard_file.html', {'form': form})


def detail(request, board_id):
    board_detail = get_object_or_404(Board, pk=board_id)
    return render(request, 'detail.html', {'board_detail': board_detail})


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