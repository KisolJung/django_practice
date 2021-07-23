from django.db import models
from django.contrib.auth.models import User

"""
null: db에 null 값을 가질지 정함 (db-related) => 문자열 기반 필드는 사용 불가능!
blank: 유효성 form.is_valid()가 호출될 대 폼 유효성 검사에 사용 (validation-related)
"""
# Create your models here.
class Board(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    pub_date = models.DateTimeField(auto_now_add=True)
    body = models.TextField()

class Comment(models.Model):
    board = models.ForeignKey(Board, on_delete=models.CASCADE, null=True)
    pub_date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    comments = models.TextField()

class UploadFile(models.Model):
    board = models.ForeignKey(Board, on_delete=models.CASCADE, null=True)
    org_file_name = models.TextField(blank=True, default="")
    file = models.FileField(blank=True, null=True, upload_to="%Y/%m/%d/")