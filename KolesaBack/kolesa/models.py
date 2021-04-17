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

class Advertisement(models.Model):
    brand = models.CharField(max_length=30)
    model = models.CharField(max_length=30)
    country = models.CharField(max_length=30)
    status = models.CharField(default="On the run", max_length=30)
    body = models.CharField(default="sedan", max_length=30)
    typeOfEngine = models.CharField(default="petrol", max_length=30)
    transmission = models.CharField(default="Automatic", max_length=30)
    steeringWheel = models.CharField(default="left", max_length=30)
    driveWheel = models.CharField(default="front-wheel drive", max_length=30)
    mileage = models.IntegerField(default=0)
    engineCapacity = models.FloatField(default=2.0)
    yearOfManufacture = models.IntegerField(default=2020)
    color = models.CharField(default="white", max_length=30)
    description = models.CharField(default="", max_length=300)
    price = models.IntegerField()
    imageBase = models.CharField(default="", max_length=300)
    image1 = models.CharField(default="", max_length=300)
    image2 = models.CharField(default="", max_length=300)
    date = models.DateTimeField(auto_now_add=True)
    user_profile = models.ForeignKey(UserProfile, on_delete=models.CASCADE, default=None)

    def __str__(self):
        return self.brand