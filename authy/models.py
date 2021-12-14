from django.contrib.auth.models import (AbstractBaseUser, BaseUserManager,
                                        PermissionsMixin)
from django.db import models


class UserManager(BaseUserManager):

    def create_user(self, nin, password=None):
        if not nin:
            raise ValueError("User must provide a NIN!")

        # email = self.normalize_email(email)
        user = self.model(nin=nin)
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, nin, password):
        user = self.create_user(nin, password)
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)

        return user


class User(AbstractBaseUser, PermissionsMixin):
    nin = models.CharField(unique=True, max_length=12, verbose_name="National Identity no")
    date_joined = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    REQUIRED_FIELDS = []
    USERNAME_FIELD = "nin"

    objects = UserManager()

    def save(self, *args, **kwargs):
        from django.db import transaction

        with transaction.atomic():
            super().save(*args, **kwargs)

            from rest_framework.authtoken.models import Token

            Token.objects.get_or_create(user=self)

    def get_full_name(self):
        return self.nin

    def get_short_name(self):
        return self.nin

    def __str__(self):
        return self.nin

    class Meta:
        db_table = 'auth_user'
        ordering = ("-created_at",)


class OTP(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='otps')
    otp = models.CharField(unique=True, max_length=4)
    created_at = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
