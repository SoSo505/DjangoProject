from django.db import models

# Create your models here.
from django.db import models

# Create your models here.
from django.contrib.auth.models import User

from auth_.models import UserProfile


class CategoryManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().order_by('category_name')


class Category(models.Model):
    category_name = models.CharField(max_length=20)
    object = CategoryManager

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.category_name


class ManufacturerManager(models.Manager):
    def get_by_brand(self):
        return super().get_queryset().order_by('brand')


class Manufacturer(models.Model):
    brand = models.CharField(max_length=30)
    model = models.CharField(max_length=30)

    object = ManufacturerManager

    def __str__(self):
        return self.brand


class CarsManager(models.Manager):
    def get_by_manufacturer(self):
        return self.filter('manufacturer')


class Cars(models.Model):
    body = models.CharField(default="sedan", max_length=30)
    transmission = models.CharField(default="Automatic", max_length=30)
    steeringWheel = models.CharField(default="left", max_length=30)
    driveWheel = models.CharField(default="front-wheel drive", max_length=30)
    numberofdoors = models.IntegerField(default=4)
    engineCapacity = models.FloatField(default=2.0)
    vin = models.IntegerField(default=123)
    description = models.CharField(default="", max_length=300)
    date = models.DateTimeField(auto_now_add=True)
    yearOfManufacture = models.IntegerField(default=2020)
    city = models.CharField(max_length=30, default='none')
    status = models.CharField(default="On the run", max_length=30)
    typeOfEngine = models.CharField(max_length=30, default='petrol')
    mileage = models.IntegerField(default=0)
    color = models.CharField(default="white", max_length=30)
    price = models.IntegerField(default=0)
    imageBase = models.ImageField(default='none')
    image1 = models.ImageField(default='none')
    image2 = models.ImageField(default='none')
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE)
    category = models.ForeignKey(Category,
                                 on_delete=models.CASCADE)

    def __str__(self):
        return self.transmission


class MototechnicsManager(models.Manager):
    def get_by_manufacturer(self):
        return self.filter('manufacturer')


class Mototechnics(models.Model):
    type = models.CharField(default="Type", max_length=30)
    engineCapacity = models.FloatField(default=0)
    yearOfManufacture = models.IntegerField(default=2020)
    city = models.CharField(max_length=30, default='none')
    status = models.CharField(default="On the run", max_length=30)
    mileage = models.IntegerField(default=0)
    price = models.IntegerField(default=0)
    imageBase = models.ImageField(default='none')
    image1 = models.ImageField(default='none')
    image2 = models.ImageField(default='none')
    # user_profile = models.ForeignKey(UserProfile, on_delete=models.CASCADE, default=None)
    category = models.ForeignKey(Category,default=1, on_delete=models.CASCADE)
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE)

    object = MototechnicsManager

    def __str__(self):
        return self.type


class TrucksManager(models.Manager):
    def get_by_manufacturer(self):
        return self.filter('manufacturer')


class Trucks(models.Model):
    type = models.CharField(default="Type", max_length=30)
    engineCapacity = models.FloatField(default=0)
    yearOfManufacture = models.IntegerField(default=2020)
    city = models.CharField(max_length=30, default='none')
    status = models.CharField(default="On the run", max_length=30)
    typeOfEngine = models.CharField(max_length=30, default="diesel fuel")
    mileage = models.IntegerField(default=0)
    price = models.IntegerField(default=0)
    imageBase = models.ImageField(default="none")
    image1 = models.ImageField(default="none")
    image2 = models.ImageField(default="none")
    # user_profile = models.ForeignKey(UserProfile, on_delete=models.CASCADE, default=None)
    category = models.ForeignKey(Category,default=3, related_name='Trucks', on_delete=models.CASCADE)
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE)

    object = TrucksManager

    def __str__(self):
        return self.type


class SpecializedTechniqueManager(models.Manager):
    def get_by_manufacturer(self):
        return self.filter('manufacturer')


class SpecializedTechnique(models.Model):

    type = models.CharField(default="Type", max_length=30)
    producing_country = models.CharField(max_length=30)
    yearOfManufacture = models.IntegerField(default=2020)
    city = models.CharField(max_length=30, default='none')
    status = models.CharField(default="On the run", max_length=30)
    typeOfEngine = models.CharField(max_length=30, default='diesel fuel')
    mileage = models.IntegerField(default=0)
    price = models.IntegerField(default=0)
    imageBase = models.ImageField(default='none')
    image1 = models.ImageField(default='none')
    image2 = models.ImageField(default='none')
    # user_profile = models.ForeignKey(UserProfile, on_delete=models.CASCADE, default=None)
    category = models.ForeignKey(Category, default='SpecializedTechnique',
                                 related_name='SpecializedTechnique', on_delete=models.CASCADE)
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE)

    object = SpecializedTechniqueManager

    def __str__(self):
        return f"{self.manufacturer}"
