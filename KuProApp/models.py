from django.utils.translation import gettext_lazy as _

from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.
class User(AbstractUser):
    class UserType(models.TextChoices):
        STANDARD = 'STANDARD', _('Standard')
        SELLER = 'SELLER', _('Seller')

    name = models.CharField(max_length=200)
    user_type = models.CharField(
        max_length=8,
        choices=UserType.choices,
        default=UserType.STANDARD,
    )

    def __str__(self):
        return f"{self.name}"


class Ad(models.Model):
    date_created = models.DateTimeField(auto_now_add=True, blank=True)
    title = models.CharField(max_length=200)
    description = models.TextField()
    price = models.FloatField()
    image = models.ImageField(upload_to="ad_photos", null=True, blank=True)
    seller_owner = models.ForeignKey(User, on_delete=models.CASCADE, default=1)

    def __str__(self):
        return f"{self.title} - by {self.seller_owner.name}"
