from django.db import models

from auth.models import MyUser, MyUserManager


class AdminManager(MyUserManager):
    pass


class AdminUser(MyUser):

    phone_number = models.IntegerField(unique=True, max_length=8)

    objects = AdminManager()

    def format_phone_number(self, phone_number):
        pass

