from django.db import models

from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
# Create your models here.BaseUserManager

class UserManager(BaseUserManager):

    def create_user(self, email, password=None):
        user = self.model(
            email=self.normalize_email(email),
            is_active=True,
            is_staff=False,
            is_superuser=False
        )

        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password=None):
        user = self.model(
            email=self.normalize_email(email),
            is_active=True,
            is_staff=True,
            is_superuser=True
        )

        user.set_password(password)
        user.save()
        return user

class User(AbstractBaseUser, PermissionsMixin):
    first_name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=30, blank=True)
    email = models.EmailField(unique=True, db_index=True)
    #-- Atributos adicionales
    phone = models.CharField(max_length=10)
    is_active = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    date_joined = models.DateTimeField(auto_now_add=True)
    
    USERNAME_FIELD = 'email'
    
    objects = UserManager()

    def __str__(self):
        return self.first_name + ' ' + self.last_name

    class Meta:
        db_table = 'users'