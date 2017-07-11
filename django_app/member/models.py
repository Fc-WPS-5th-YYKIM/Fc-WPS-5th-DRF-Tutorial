from django.contrib.auth.models import AbstractUser
from django.db import models


class MyUser(AbstractUser):
    # 나중에 AbstractBaseUser를 상속받아 CustomUser만들기 해보세요
    pass
