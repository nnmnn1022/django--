from django.db import models
from config.models import BaseModel
# from django.contrib.auth.models import BaseUserManager, AbstractBaseUser

# class UserManager(BaseUserManager) : # User Model을 커스텀하기 위한 Helper클래스
#     def create_user(self,name, email, gmail, password=None):
#         if not email or not gmail or not name:
#             raise ValueError('항목을 모두 입력해야 합니다.')

#         user = self.model(
#             name = self.name,
#             email = self.normalize_email(email),
#             gmail = self.normalize_email(gmail),
#         )

#         user.set_password(password)
#         user.save(using=self._db)
#         return user

#     def create_superuser(self,name, email, gmail, password):
#         user = self.create_user(
#             name,
#             email,
#             gmail,
#             password=password,
#         )
#         user.is_admin = True
#         user.save(using=self._db)
#         return user


# class UserModel(AbstractBaseUser, BaseModel):
#     name = models.CharField(
#         verbose_name='이름',
#         max_length=10,
#         unique=True,
#     )
#     email = models.EmailField(
#         verbose_name='email',
#         max_length=255,
#         unique=True,
#     )

#     gmail = models.EmailField(
#         verbose_name='gmail',
#         max_length=255,
#         unique=True,
#     )
    
#     is_active = models.BooleanField(default=True)
#     is_admin = models.BooleanField(default=False)

#     objects = UserManager()

#     USERNAME_FIELD = 'email'
#     REQUIRED_FIELDS = ['name','gmail',]

#     def __str__(self):
#         return self.email

#     def has_perm(self, perm, obj=None):
#         return True

#     def has_module_perms(self, app_label):
#         return True

#     @property
#     def is_staff(self):
#         return self.is_admin

