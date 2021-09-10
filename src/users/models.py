from django.contrib.auth.models import AbstractUser
from django.db import models



class UserProfile(AbstractUser):
    email = models.EmailField(max_length=255, unique=True)