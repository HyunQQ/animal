from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin


class AnimalUser(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100, unique=True)
    location = models.CharField(max_length=200)
    interest = models.CharField(max_length=200, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.name}, {self.email}'


class AnimalUserManager(BaseUserManager):
    use_in_migrations = True

    def create_user(self, email, name, password):

        if not email:
            raise ValueError('must have user email')
        user = self.model(
            email=self.normalize_email(email),
            name=name
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, name, password):
        user = self.create_user(
            email=self.normalize_email(email),
            name=name,
            password=password
        )
        user.is_admin = True
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)
        return user


class AnimalUser(AbstractBaseUser, PermissionsMixin):
    objects = AnimalUserManager()

    email = models.EmailField(
        max_length=255,
        unique=True,
    )
    name = models.CharField(
        max_length=50,
        null=False,
        unique=True
    )

    location = models.CharField(max_length=200)
    interest = models.CharField(max_length=200, blank=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    date_joined = models.DateTimeField(auto_now_add=True)
    USERNAME_FIELD = 'name'
    REQUIRED_FIELDS = ['email']