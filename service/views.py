from django.shortcuts import render
from .serializers import *
from .models import *
from rest_framework import viewsets

# Create your views here.
class NotificationViewSet(viewsets.ModelViewSet):
    queryset = Notification.objects.all()
    serializer_class = NotificationSerializer


class NotificationTypeViewSet(viewsets.ModelViewSet):
    queryset = NotificationType.objects.all()
    serializer_class = NotificationTypeSerializer


class NotificationSettingViewSet(viewsets.ModelViewSet):
    queryset = NotificationSetting.objects.all()
    serializer_class = NotificationSettingSerializer


class UserNotificationViewSet(viewsets.ModelViewSet):
    queryset = UserNotification.objects.all()
    serializer_class = UserNotificationSerializer


class NotificationManagementViewSet(viewsets.ModelViewSet):
    queryset = NotificationManagement.objects.all()
    serializer_class = NotificationManagementSerializer