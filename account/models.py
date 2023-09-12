from django.db import models
from django.db import connections
from django.contrib.auth.models import AbstractUser
from Role_based_login_system import settings

author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)


# Create your models here.


class User(AbstractUser):
    is_admin = models.BooleanField('Is admin', default=False)
    is_customer = models.BooleanField('Is customer', default=True)
    is_employee = models.BooleanField('Is employee', default=False)


class Userdetails(models.Model):
    username = models.CharField(max_length=256)
    email = models.CharField(max_length=256)

    class Meta:
        db_table = "account_user"
        managed = False
        unique_together = (('username', 'email'),)

