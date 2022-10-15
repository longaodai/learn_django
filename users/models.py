from django.db import models
from django.contrib.auth.models import User


class UserModel(User):
    phone = models.CharField(max_length=10)
    address = models.CharField(max_length=225)

    def __str__(self):
        return self.username

    class Meta:
        ordering = ['-id']
