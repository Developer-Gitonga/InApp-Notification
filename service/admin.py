from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Notification)
admin.site.register(NotificationType)
admin.site.register(NotificationSetting)
admin.site.register(UserNotification)
admin.site.register(NotificationManagement)

