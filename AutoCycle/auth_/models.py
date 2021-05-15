from django.contrib.auth.models import User
from django.db import models


class UserProfileManager(models.Manager):
    def create_user_profile(self, user, phoneNumber):
        userProfile = self.create(user=user)
        userProfile.phoneNumber = phoneNumber
        userProfile.save()
        return userProfile


class UserProfile(models.Model):
    phoneNumber = models.CharField(max_length=12)
    join_date = models.DateTimeField(auto_now_add=True, null=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE, default=None)

    objects = UserProfileManager()

    def __str__(self):
        return self.user.username
