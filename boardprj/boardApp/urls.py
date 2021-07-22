from django.urls import path
from . import views

app_name = 'boardApp'

urlpatterns = [
    path('', views.boardMain, name='boardMain'),
    #path('createBoard/', views.createBoard, name='createBoard'),
    #path('sampleUpload/', views.uploadFile, name='uploadFile'),
    path('boardWfile/', views.createBoard_File, name='createBoard_File'),
    path('detail/<int:board_id>/', views.detail, name='detail'),
]