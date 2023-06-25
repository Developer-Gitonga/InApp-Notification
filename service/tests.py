from django.test import TestCase
from django.utils import timezone
from .models import Notification
from django.contrib.auth.models import User

class NotificationModelTestCase(TestCase):
    def setUpTestData(cls):
        # Create a test user
        cls.notification = Notification.objects.create(
           content='Test notification'
        )

    def test_notification_content(self):
        notification = Notification.objects.get(id=self.notification.id)
        self.assertEqual(notification.content, 'Test notification')

    # def test_notification_timestamp(self):
    #     notification = Notification.objects.get(id=1)
    #     self.assertIsNotNone(notification.timestamp)

    # def test_notification_sender(self):
    #     notification = Notification.objects.get(id=1)
    #     sender = User.objects.get(username='testuser')
    #     self.assertEqual(notification.sender, sender)

    # def test_notification_recipient(self):
    #     notification = Notification.objects.get(id=1)
    #     recipient = User.objects.get(username='testuser')
    #     self.assertEqual(notification.recipient, recipient)  # Corrected field name

    # def test_notification_is_read(self):
    #     notification = Notification.objects.get(id=1)
    #     self.assertFalse(notification.is_read)
