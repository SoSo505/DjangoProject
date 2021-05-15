from django.contrib import admin

# Register your models here.
from auth_.models import UserProfile

admin.site.register(UserProfile)
