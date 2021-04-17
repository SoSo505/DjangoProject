from django.core.exceptions import EmptyResultSet
from django.shortcuts import redirect
from django.views.decorators.csrf import csrf_exempt
from rest_framework.response import Response
from rest_framework import generics, status
from django.http import Http404
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAdminUser, IsAuthenticated, AllowAny

from kolesa.models import Advertisement, UserProfile
from kolesa.serializers import AdvertisementSerializer, UserSerializer, UserProfileSerializer

class AdvertisementList(generics.ListAPIView):
    serializer_class = AdvertisementSerializer
    queryset = Advertisement.objects.all()
    permission_classes = [AllowAny]

@api_view(['GET'])
@permission_classes((AllowAny))
def advertisement_list(request):
    if request.method == 'GET':
        advertisements = Advertisement.objects.all()
        serializer = AdvertisementSerializer(advertisements, many=True)
        return Response(serializer.data)



class AdvertisementDetail(generics.RetrieveAPIView):
    serializer_class = AdvertisementSerializer
    queryset = Advertisement.objects.all()
    permission_classes = [AllowAny]

@api_view(['GET'])
@permission_classes((AllowAny))
def advertisement_detail(request, advertisement_id):
    try:
        advertisement = Advertisement.objects.get(id=advertisement_id)
    except Advertisement.DoesNotExist as e:
        return Response({'error': str(e)})

    if request.method == 'GET':
        serializer = AdvertisementSerializer(advertisement)
        return Response(serializer.data)

class UserProfileList(generics.ListAPIView):
    serializer_class = UserProfileSerializer
    queryset = UserProfile.objects.all()
    permission_classes = [IsAdminUser]

class MyAdvertisements(generics.ListCreateAPIView):
    serializer_class = AdvertisementSerializer
    def get_queryset(self):
        try:
            advertisements = Advertisement.objects.all().filter(user_profile__user=self.request.user)
        except EmptyResultSet:
            raise Http404
        return advertisements
    permission_classes = [IsAuthenticated]

class MyAdvertisementDetail(generics.RetrieveDestroyAPIView):
    serializer_class = AdvertisementSerializer
    def get_queryset(self):
        try:
            advertisements = Advertisement.objects.all().filter(user_profile__user=self.request.user)
        except EmptyResultSet:
            raise Http404
        return advertisements
    permission_classes = [IsAuthenticated]

# class MyAdvertisementDetail(generics.RetrieveUpdateDestroyAPIView):
#     serializer_class = AdvertisementSerializer
#     def get_queryset(self):
#         try:
#             advertisements = Advertisement.objects.all().filter(user_profile__user=self.request.user)
#         except EmptyResultSet:
#             raise Http404
#         return advertisements
#     permission_classes = [IsAuthenticated]

class MyProfile(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = UserProfileSerializer
    def get_object(self):
        try:
            profile = UserProfile.objects.get(user=self.request.user)
        except EmptyResultSet:
            raise Http404
        return profile
    permission_classes = [IsAuthenticated]

@csrf_exempt
def redirect_view(request):
    return redirect('kolesa.kz/advertisements')

class BrandAdvertisements(generics.ListAPIView):
    serializer_class = AdvertisementSerializer
    def get_queryset(self):
        try:
            advertisements = Advertisement.objects.all().filter(brand = self.kwargs.get('brand'))
        except EmptyResultSet:
            raise Http404
        queryset = []
        for advertisement in advertisements:
            queryset.append(advertisement)
        return queryset
    permission_classes = [AllowAny]

class BrandModelAdvertisements(generics.ListAPIView):
    serializer_class = AdvertisementSerializer
    def get_queryset(self):
        try:
            advertisements = Advertisement.objects.all().filter(brand = self.kwargs.get('brand'), model = self.kwargs.get('model'))
        except EmptyResultSet:
            raise Http404
        queryset = []
        for advertisement in advertisements:
            queryset.append(advertisement)
        return queryset
    permission_classes = [AllowAny]

class BrandModelYearAdvertisements(generics.ListAPIView):
    serializer_class = AdvertisementSerializer
    def get_queryset(self):
        try:
            advertisements = Advertisement.objects.all().filter(brand = self.kwargs.get('brand'),
                                            model = self.kwargs.get('model'), yearOfManufacture = self.kwargs.get('year'))
        except EmptyResultSet:
            raise Http404
        queryset = []
        for advertisement in advertisements:
            queryset.append(advertisement)
        return queryset
    permission_classes = [AllowAny]