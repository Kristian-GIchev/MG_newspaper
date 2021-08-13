from django.contrib.auth import get_user_model
from django.db import models
from cloudinary.models import CloudinaryField
UserModel = get_user_model()


class Profile(models.Model):
    first_name = models.CharField(
        max_length=20,
        blank=True
    )

    last_name = models.CharField(
        max_length=20,
        blank=True
    )

    profile_pic = CloudinaryField("Profile Picture", blank=True, null=True)

    age = models.IntegerField(
        null=True,
        blank=True,
    )

    user = models.OneToOneField(
        UserModel,
        on_delete=models.CASCADE,
        primary_key=True,
    )

    is_complete = models.BooleanField(
        default=False
    )
