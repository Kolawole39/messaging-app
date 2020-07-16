from django.db import models

from auth.models import MyUserManager, MyUser


class ChatterManager(MyUserManager):
    pass


class Chatter(MyUser):
    phone_number = models.IntegerField(null=True, verbose_name='Phone number')

    objects = ChatterManager()

    def format_phone_number(self):
        pass
