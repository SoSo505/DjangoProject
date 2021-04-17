from .serializers import UserSerializer, UserProfileSerializerSignUp
from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated
from .models import UserProfile
from rest_framework import status

@api_view(['POST'])
def login(request):
    serializer = AuthTokenSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    user = serializer.validated_data.get('user')
    token, created = Token.objects.get_or_create(user=user)

    return Response({'token': token.key})


@api_view(['POST'])
def logout(request):
    request.auth.delete()
    return Response('Successfully deleted')

@api_view(['POST'])
def signup(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        user = User.objects.create_user(
            username = serializer.data['username'],
            email = serializer.data['email'],
            password = serializer.data['password']
        )
        serializer2 = UserProfileSerializerSignUp(data=request.data)
        if serializer2.is_valid():
            userProfile = UserProfile.objects.create_user_profile(user=user, phoneNumber=serializer2.data['phoneNumber'])
            return Response(serializer2.data, status=status.HTTP_200_OK)
    return Response(serializer.errors)