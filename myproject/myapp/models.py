from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator


class CustomUser(AbstractUser):
    number_phone_regex = RegexValidator(regex=r"^\+?1?\d{8,15}$")
    number_phone = models.CharField(validators=[number_phone_regex], max_length=16, unique=True)
