from django import forms
from django.forms import ClearableFileInput
from .models import Board, Comment, UploadFile
from ckeditor_uploader.widgets import CKEditorUploadingWidget

#Meta 클래스는 내부 클래스로 활용되며, 기본필드의 값을 재정의 할 때 사용.

class CreateBoard(forms.ModelForm):
    class Meta:
        model = Board
        fields = ['title', 'body']

        widgets = {
            'title': forms.TextInput(
                attrs={'placeholder': '제목을 입력하세요.'}),
            'body': forms.CharField(widget=CKEditorUploadingWidget())
        }


class CreateComment(forms.ModelForm):
    class Meta:
        model = Comment
        fields=['comments']
        widgets = {
            'comments': forms.Textarea(attrs={'class':'form-control', 'rows': 4, 'cols': 40, 'placeholder': 'Join the discussion and Leave a comments!'})
        }

class UploadFileForm(forms.ModelForm):
    class Meta:
        model = UploadFile
        fields = ['file']
        widgets = {
            'file': ClearableFileInput(attrs={'multiple': True, 'style': 'border: 1px solid'})
        }