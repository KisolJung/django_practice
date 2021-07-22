from django import forms
from .models import Board, Comment

#Meta 클래스는 내부 클래스로 활용되며, 기본필드의 값을 재정의 할 때 사용.

class CreateBoard(forms.ModelForm):
    class Meta:
        model = Board
        fields = ['title', 'body', 'file_path', 'file_name']

        widgets = {
            'title': forms.TextInput(
                attrs={'placeholder': '제목을 입력하세요.'}),
            'file_name': forms.HiddenInput(),
            'file_path': forms.FileInput(attrs={'style': 'border: 1px solid'})
        }


class CreateComment(forms.ModelForm):
    class Meta:
        model = Comment
        fields=['comments']
        widgets = {
            'comments': forms.Textarea(attrs={'class':'form-control', 'rows': 4, 'cols': 40, 'placeholder': 'Join the discussion and Leave a comments!'})
        }
