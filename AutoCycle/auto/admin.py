from django.contrib import admin
from auto.models import Cars, Manufacturer, Trucks, Mototechnics, SpecializedTechnique

# Register your models here.
admin.site.register(Cars)
admin.site.register(Manufacturer)
admin.site.register(Trucks)
admin.site.register(Mototechnics)
admin.site.register(SpecializedTechnique)
