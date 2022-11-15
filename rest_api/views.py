from rest_framework import status
from .models import UserProfile
from rest_framework.response import Response
from .serializers import UserProfileSerializer
from rest_framework import viewsets
from rest_framework.viewsets import ModelViewSet


class UserProfileView(ModelViewSet):
    serializer_class = UserProfileSerializer
    queryset = UserProfile.objects.all()
