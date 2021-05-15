from django.conf import settings
from django.contrib.auth.views import LogoutView
from django.urls import path

from auto.views import MyAdvertisements, ManufacturerViewSet, CategoryViewSet, CarsViewSet, MototechnicsApiView, \
    trucks_list, MototechnicsDetailApiView, truck_detail, SpecializedTechniqueApiView, CarBrandAdvertisements, \
    CarBrandModelAdvertisements, CarByYearViewSet, MototechnicsByTypeViewSet, MototechnicsByBrandViewSet, \
    MototechnicsByBrandModelViewSet, SpecializedTechniqueByTypeApiView, SpecializedTechniqueByBrandApiView, \
    TrucksByBrandApiView, TrucksByTypeViewSet, SpecializedTechniqueTypeViewSet, SpecializedTechniqueDetailApiView


class SpecializedTechniqueByBrandViewSet(object):
    pass


urlpatterns = [

    path('category/', CategoryViewSet.as_view({'get': 'list', 'post': 'create'})),

    path('advertisements/manufacturer/',
         ManufacturerViewSet.as_view({'get': 'list', 'post': 'create', 'delete': 'destroy'})),

    path('cars/', CarsViewSet.as_view({'get': 'list', 'post': 'create'})),
    path('cars/<int:pk>/', CarsViewSet.as_view({'get':'retrieve', 'post': 'update', 'delete': 'destroy'})),
    path('cars/year/<int:year>/', CarByYearViewSet.as_view({'get': 'list'})),
    path('cars/<str:brand>/', CarBrandAdvertisements.as_view()),
    path('cars/<str:brand>/<str:model>/', CarBrandModelAdvertisements.as_view()),

    path('mototechnics/', MototechnicsApiView.as_view()),
    path('mototechnics/<int:pk>', MototechnicsDetailApiView.as_view()),
    path('mototechnics/<str:brand>', MototechnicsByBrandViewSet.as_view({'get': 'list'})),
    path('mototechnics/<str:brand>/<str:model>/', MototechnicsByBrandModelViewSet.as_view({'get': 'list'})),
    path('mototechnics/type/<str:type>', MototechnicsByTypeViewSet.as_view({'get': 'list'})),
    

    path('trucks/', trucks_list, name='trucks_list'),
    path('trucks/<int:pk>/', truck_detail, name='truck_detail'),
    path('trucks/type/<str:type>/', TrucksByTypeViewSet.as_view({'get': 'list'})),
    path('trucks/<str:brand>/', TrucksByBrandApiView.as_view()),

    path('specializedtechnique/', SpecializedTechniqueApiView.as_view()),
    path('specializedtechnique/<int:pk>/', SpecializedTechniqueDetailApiView.as_view()),
    path('specializedtechnique/type/<str:type>/', SpecializedTechniqueTypeViewSet.as_view({'get': 'list'})),
    path('specializedtechnique/<str:brand>/', SpecializedTechniqueByBrandApiView.as_view()),

]
