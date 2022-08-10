import json
from channels.generic.websocket import WebsocketConsumer, AsyncWebsocketConsumer 
from channels.db import database_sync_to_async 
from asgiref.sync import async_to_sync,sync_to_async 
from channels.layers import get_channel_layer
from .models import Notifications
from django.forms.models import model_to_dict
from time import sleep
import django.db.models.signals.post_save


#@database_sync_to_async
def get_last_notification():
    try:
        return Notifications.objects.last()
    except:
        return Notifications.objects.get()


class NotificationConsumer(WebsocketConsumer):
    def connect(self):
        print(self.scope)
        self.accept()
        while True:
            self.send(json.dumps({
                "type":"websocket.send",
                "text": model_to_dict(Notifications.objects.last())
            })) 
            sleep(1)