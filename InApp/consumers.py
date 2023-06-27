from channels.generic.websocket import AsyncWebsocketConsumer
import asyncio

class NotificationConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        # Perform necessary connection setup tasks
        await self.accept()

    async def disconnect(self, close_code):
        # Perform necessary connection cleanup tasks
        pass

    async def receive(self, text_data):
        # Handle received data, if needed
        pass

    async def notify(self, event):
        # Send notification data to the client
        await self.send(text_data=event["text"])
