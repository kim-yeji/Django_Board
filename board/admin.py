from django.contrib import admin
from .models import Post
from board.models import Board


class BoardAdmin(admin.ModelAdmin):
    #관리자 페이지에 표시할 필드 목록을 튜플 형식으로 선언
    list_display = ("writer", "title", "content")


admin.site.register(Board, BoardAdmin) #관리자 사이트에서 사용할 수 있도록 테이블 등록
admin.site.register(Post)