from channels.routing import ProtocolTypeRouter, URLRouter
from django.urls import path
from notifications.consumers import NotificationConsumer

application = ProtocolTypeRouter(
    {
        "http": get_asgi_application(),
        "websocket": AuthMiddlewareStack(
            URLRouter(
                [
                    path("ws/notifications/", NotificationConsumer.as_asgi()),
                ]
            )
        ),
    }
)
