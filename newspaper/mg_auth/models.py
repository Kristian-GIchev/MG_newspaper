from django.contrib.auth.base_user import BaseUserManager, AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin, UserManager, AbstractUser
from django.contrib.auth.hashers import make_password
from django.contrib.contenttypes.models import ContentType
from django.db import models


class MgUserManager(BaseUserManager):
    def _create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError('The given email must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.password = make_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, **extra_fields)

    def create_superuser(self, email, password=None,  **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(email, password, **extra_fields)


class MgUser(AbstractBaseUser, PermissionsMixin):

    email = models.EmailField(
        unique=True,
    )

    USERNAME_FIELD = 'email'

    is_staff = models.BooleanField(
        default=False,
    )

    objects = MgUserManager()

    @property
    def username(self):
        profile_username = self.profile.username
        first = self.profile.first_name
        last = self.profile.last_name
        if profile_username:
            username = profile_username
        elif not profile_username and first and last:
            username = first + " " + last
        else:
            username = self.email
        return username
