# -*- coding: utf-8 -*-

from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager
from django.db import models


class UserManager(BaseUserManager):

    def create_user(self, email, password=None):
        if not email:
            raise ValueError(u'Email непременно должен быть указан')

        user = self.model(
            email=UserManager.normalize_email(email),
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password):
        user = self.create_user(email, password)
        user.is_admin = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class ExtUser(AbstractBaseUser, PermissionsMixin):

    email = models.EmailField(
        u'Электронная почта',
        max_length=255,
        unique=True,
        db_index=True
    )
    avatar = models.ImageField(
        u'Аватар',
        blank=True,
        null=True,
        upload_to="uploads/user_avatars/"
    )
    firstname = models.CharField(
        u'Фамилия',
        max_length=40,
        null=True,
        blank=True
    )
    lastname = models.CharField(
        u'Имя',
        max_length=40,
        null=True,
        blank=True
    )
    middlename = models.CharField(
        u'Отчество',
        max_length=40,
        null=True,
        blank=True
    )
    date_of_birth = models.DateField(
        u'Дата рождения',
        null=True,
        blank=True
    )
    register_date = models.DateField(
        u'Дата регистрации',
        auto_now_add=True
    )
    is_active = models.BooleanField(
        u'Активен',
        default=True
    )
    is_admin = models.BooleanField(
        u'Суперпользователь',
        default=False
    )

    # Этот метод обязательно должен быть определён
    def get_full_name(self):
        return self.email

    # Требуется для админки
    @property
    def is_staff(self):
        return self.is_admin

    def get_short_name(self):
        return self.email

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()

    class Meta:
        verbose_name = u'Пользователь'
        verbose_name_plural = u'Пользователи'
