from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    username = models.CharField(max_length=25, unique=True)
    is_active = models.BooleanField(default=True)

    USERNAME_FIELD = 'username'

    def __str__(self):
        return self.username
