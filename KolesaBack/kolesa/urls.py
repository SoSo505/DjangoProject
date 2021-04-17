from django.conf import settings
from django.contrib.auth.views import LogoutView
from django.urls import path

from kolesa import auth
from kolesa.views import AdvertisementList, AdvertisementDetail, BrandAdvertisements, BrandModelAdvertisements, \
    BrandModelYearAdvertisements, MyProfile, MyAdvertisements, MyAdvertisementDetail, UserProfileList

urlpatterns = [
    path('advertisements/', AdvertisementList.as_view()),
    path('advertisements/<int:pk>/', AdvertisementDetail.as_view()),
    path('advertisements/<str:brand>/', BrandAdvertisements.as_view()),
    path('advertisements/<str:brand>/<str:model>/', BrandModelAdvertisements.as_view()),
    path('advertisements/<str:brand>/<str:model>/<int:year>', BrandModelYearAdvertisements.as_view()),

    path('login/', auth.login),
    path('logout/', LogoutView.as_view(), {'next_page': settings.LOGOUT_REDIRECT_URL}, name='logout'),
    path('signup/', auth.signup),
    path('my_profile/', MyProfile.as_view()),
    path('my_advertisements/', MyAdvertisements.as_view()),
    path('my_advertisements/<int:pk>/', MyAdvertisementDetail.as_view()),

    path('profiles/', UserProfileList.as_view())
]
