from django.contrib.auth.models import AbstractUser
from django.db import models


# Custom User model that will be used to keep track of a user's profile info
class CustomUser(AbstractUser):
    weather_location = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.username
