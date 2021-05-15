from rest_framework import serializers
from django.contrib.auth.models import User
from auth_.models import UserProfile


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'password', 'email')


class UserProfileSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    user = UserSerializer()

    class Meta:
        model = UserProfile
        fields = '__all__'


class UserProfileSerializerSignUp(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = UserProfile
        fields = ('id', 'phoneNumber', 'user')
