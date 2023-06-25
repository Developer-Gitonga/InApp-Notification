from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Notification(models.Model):
    content = models.TextField()
    timestamp = models.DateTimeField()
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sent_notifications')
    recepient = models.ForeignKey(User, on_delete=models.CASCADE, related_name='received_notification')
    is_read = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class NotificationType(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()


class NotificationSetting(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    notification_type = models.ForeignKey(NotificationType, on_delete=models.CASCADE)
    delivery_method = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class UserNotification(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    notification = models.ForeignKey(Notification, on_delete=models.CASCADE)
    is_read = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class NotificationManagement(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    delivery_rate = models.FloatField()
    user_engagement = models.FloatField()
    template = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)