from django.db import models
from django.contrib.auth.models import AbstractUser, UserManager as DjangoUserManager

# Manager는 DB로 쿼리를 날릴 때 Django가 제공하는 인터페이스


class UserManager(DjangoUserManager):
    def _create_user(self, email, name, password, **extra_fields):
        if not email:
            raise ValueError('The given email must be set')
        if not name:
            raise ValueError('이름은 필수 값입니다.')
        user = self.model(email=self.normalize_email(
            email), name=name, **extra_fields)
        # 해싱을 해서 넣는 이유 (암호화, 복호화) : 비밀번호를 관리자도 알 수 없게 하기 위해.
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, name, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, name, password, **extra_fields)

    def create_superuser(self, email, name, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')
        return self._create_user(email, name, password, **extra_fields)


class User(AbstractUser):
    email = models.EmailField(verbose_name='E-mail(ID)', unique=True)
    name = models.CharField(verbose_name='이름', max_length=10, blank=False)
    profile_image = models.ImageField(
        verbose_name='프로필 사진', blank=True, null=True)
    gmail = models.EmailField(verbose_name='Gmail 주소')
    l10n = models.CharField(verbose_name='담당 언어',
                            blank=True,
                            null=True,
                            max_length=2,
                            )
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    # 커스터마이징한 usermanager 모델을 연결
    objects = UserManager()
