from django.conf import settings
from django.contrib.auth.views import LogoutView
from django.urls import path
from auth_ import auth
from auth_.views import MyProfile, MyAdvertisements, MyAdvertisementDetail, UserProfileList

urlpatterns = [
    path('login/', auth.login),
    path('logout/', LogoutView.as_view(), {'next_page': settings.LOGOUT_REDIRECT_URL}, name='logout'),
    path('signup/', auth.signup),
    path('my_profile/', MyProfile.as_view()),
    path('my_advertisements/', MyAdvertisements.as_view()),
    path('my_advertisements/<int:pk>/', MyAdvertisementDetail.as_view()),

    path('profiles/', UserProfileList.as_view())
]
