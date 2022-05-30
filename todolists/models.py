from django.db import models
from django.contrib.auth import get_user_model
from config.models import BaseModel

User = get_user_model()

class ToDoList(BaseModel):
    # 작성일 created_at 상속
    # 수정일 modified_at 상속
    checkbox = models.BooleanField(verbose_name='완료 여부')    # 체크박스
    content = models.CharField(verbose_name='할 일', max_length=64)  # 할 일
    created_by = models.ForeignKey(to=User, related_name='todolist_writer',
                                   on_delete=models.CASCADE, verbose_name='작성자', blank=True)    # 작성자
    worker = models.ForeignKey(
        to=User, related_name='worker', on_delete=models.CASCADE, verbose_name='담당자')
    deadline = models.DateTimeField(verbose_name='기한',)
    # work_by =  다른 유저에게 할당하는 부분이 있어야 할 것으로 보임
    content_detail = models.TextField(verbose_name='세부내용')  # 세부 내용
