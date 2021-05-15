from django.core.exceptions import EmptyResultSet
from django.http import Http404
from django.shortcuts import render

# Create your views here.
from rest_framework import status, generics
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.decorators import api_view
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response

from auth_.serializers import UserSerializer, UserProfileSerializerSignUp, UserProfileSerializer
from auto.models import Cars
from auto.serializers import CarsSerializer

from .models import UserProfile



class MyProfile(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = UserProfileSerializer

    def get_object(self):
        try:
            profile = UserProfile.objects.get(user=self.request.user)
        except EmptyResultSet:
            raise Http404
        return profile

    permission_classes = [IsAuthenticated]


class MyAdvertisements(generics.ListCreateAPIView):
    serializer_class = CarsSerializer

    def get_queryset(self):
        try:
            advertisements = Cars.objects.all().filter(user=self.request.user)
        except EmptyResultSet:
            raise Http404
        return advertisements

    permission_classes = [IsAuthenticated]


class MyAdvertisementDetail(generics.RetrieveDestroyAPIView):
    serializer_class = CarsSerializer

    def get_queryset(self):
        try:
            advertisements = Cars.objects.all().filter(userProfile__user=self.request.user)
        except EmptyResultSet:
            raise Http404
        return advertisements

    permission_classes = [IsAuthenticated]


class UserProfileList(generics.ListAPIView):
    serializer_class = UserProfileSerializer
    queryset = UserProfile.objects.all()
    permission_classes = [IsAdminUser]
