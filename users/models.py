from django.db import models
from django.contrib.auth.models import AbstractUser, UserManager as DjangoUserManager

# Manager는 DB로 쿼리를 날릴 때 Django가 제공하는 인터페이스


class UserManager(DjangoUserManager):
    def _create_user(self, email, name, password, **extra_fields):
        if not name:
            raise ValueError('이름은 필수 값입니다.')
        user = self.model(username=email, name=name)
        # 해싱을 해서 넣는 이유 (암호화, 복호화) : 비밀번호를 관리자도 알 수 없게 하기 위해.
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, username, email=None, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(username, email, password, **extra_fields)

    def create_superuser(self, username, email=None, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self._create_user(username, email, password, **extra_fields)


class User(AbstractUser):
    email = models.EmailField(verbose_name='E-mail(ID)' unique=True)
    name = models.CharField(verbose_name='이름', max_length=10)
    profile_image = models.ImageField(
        verbose_name='프로필 사진', blank=True, null=True)
    email = models.EmailField(verbose_name='Gmail 주소')
    USERNAME_FIELD = 'email'

    # 커스터마이징한 usermanager 모델을 연결
    objects = UserManager()
