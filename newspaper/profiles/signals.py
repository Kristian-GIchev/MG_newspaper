from django.contrib.auth import get_user_model
from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver

from newspaper.profiles.models import Profile

UserModel = get_user_model()


@receiver(post_save, sender=UserModel)
def user_created(sender, instance, created, **kwargs):
    if created:
        profile = Profile.objects.create(user=instance)
        profile.save()


@receiver(pre_save, sender=Profile)
def check_is_complete(sender, instance, **kwargs):
    if instance.first_name and instance.last_name and instance.age and instance.profile_pic:
        instance.is_complete = True
    else:
        instance.is_complete = False


# @receiver(pre_save, sender=Profile)
# def remove_image_from_cloudinary_too(sender, instance, **kwargs):
#     if not instance.profile_pic:
