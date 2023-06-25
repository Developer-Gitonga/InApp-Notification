from rest_framework import serializers
from .models import *

# Create your serializers here.
class NotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notification
        fields = '__all__'


class NotificationTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = NotificationType
        fields = '__all__'


class NotificationSettingSerializer(serializers.ModelSerializer):
    class Meta:
        model = NotificationSetting
        fields = '__all__'


class UserNotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserNotification
        fields = '__all__'


class NotificationManagementSerializer(serializers.ModelSerializer):
    class Meta:
        model = NotificationManagement
        fields = '__all__'