from django.db import models
from django.contrib.auth import get_user_model

class BaseModel(models.Model) :
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='생성일시')
    modified_at = models.DateTimeField(auto_now=True, verbose_name='수정일시')

    class Meta :
        abstract = True