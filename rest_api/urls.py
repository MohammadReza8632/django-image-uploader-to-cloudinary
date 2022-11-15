from rest_framework import routers
from rest_framework.routers import DefaultRouter
from .views import UserProfileView
from django.urls import path, include
router = DefaultRouter()
router.register('user-profile', UserProfileView)

urlpatterns = [
    path('', include(router.urls)),
]
