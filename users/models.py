from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    # Acrescentar os campos necessários do usuario
    #bio = models.TextField(blank=True)
    pass