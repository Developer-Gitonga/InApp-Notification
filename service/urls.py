from django.urls import path
from .views import *
from rest_framework import viewsets

app_name = 'service'

# Create your urls here.
urlpatterns = [
    path('notification/', NotificationViewSet.as_view({'get': 'list', 'post': 'create'}), name = "notification"),
    path('notification-setting/', NotificationSettingViewSet.as_view({'get': 'list', 'post': 'create'}),name = "notification-setting"),
    path('notification-type/', NotificationTypeViewSet.as_view({'get': 'list', 'put': 'update', 'patch': 'partial_update', 'delete': 'destroy'}), name = "notification-type"),
    path('user-notification/', UserNotificationViewSet.as_view({'get': 'list', 'put': 'update', 'patch': 'partial_update', 'delete': 'destroy'}),name = "user-notification"),
    path('notification-management/', NotificationManagementViewSet.as_view({'get': 'list', 'post': 'create', 'put': 'update', 'patch': 'partial_update', 'delete': 'destroy'}), name = "notification-management"),
]