from django.db.models.signals import post_delete, post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from auth_.models import UserProfile


# @receiver(post_save, sender=User)
# def create_user_profile_or_safe(sender, instance, created, **kwargs):
#     if created:
#         UserProfile.objects.create(user=instance)
#     instance.user.save()
#

# @receiver(post_save, sender = User)
# def add_score(instance, **kwargs):
#     profile = instance.user_profile
#     profile.score += 1
#     profile.save()