from django.urls import path
from . import views

app_name = 'boardApp'

urlpatterns = [
    path('', views.boardMain, name='boardMain'),
    path('createBoard/', views.create_board_multiFile, name='create_board_multiFile'),
    path('detail/<int:board_id>/', views.detail, name='detail'),
]