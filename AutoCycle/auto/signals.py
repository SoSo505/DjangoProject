from django.db.models.signals import post_delete, post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from auth_.models import UserProfile
from auto.models import Category


@receiver(post_save, sender=Category)
def delete_category_on_cars(sender, instance, **kwargs):
    instance.category.delete()


@receiver(post_save, sender=Category)
def delete_manufacturer_on_cars(sender, instance, **kwargs):
    instance.manufacturer.delete()
