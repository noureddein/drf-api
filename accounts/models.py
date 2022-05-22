from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    phone_number = models.CharField(max_length=10, blank=True, null=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    user_type = models.CharField(
        max_length=10,
        choices=(
            ('buyer', 'Buyer'),
            ('seller', 'Seller')
        )
    )

    def __str__(self):
        return self.email
