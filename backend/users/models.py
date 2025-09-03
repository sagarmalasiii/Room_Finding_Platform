from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    class Roles(models.TextChoices):
        ADMIN = "ADMIN", "Admin"
        SEEKER = "SEEKER", "Seeker"
        LANDLORD = "LANDLORD", "Landlord"

    role = models.CharField(
        max_length=10,
        choices=Roles.choices,
        default=Roles.SEEKER,  # most new users are seekers
    )
