from django.contrib import admin
from django.urls import path, include

from kolesa.views import redirect_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('kolesa.kz/base-auth', include('rest_framework.urls')),
    path('kolesa.kz/', include('kolesa.urls')),
    path('', redirect_view)
]
